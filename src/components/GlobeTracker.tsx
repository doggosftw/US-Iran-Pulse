import { useEffect, useRef, useState, useMemo, useCallback, memo } from 'react';
import Globe from 'react-globe.gl';
import * as THREE from 'three';
import type { PulseEvent } from '../App';

const GEOJSON_URL = '/countries.geojson';
const EMPTY_ARRAY: any[] = [];

// Inject global styles for the pulsing HTML element gracefully
const injectStyles = () => {
    if (!document.getElementById('globe-pulsing-style')) {
        const style = document.createElement('style');
        style.id = 'globe-pulsing-style';
        style.innerHTML = `
            @keyframes globe-pulse {
                0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(250, 204, 21, 0.7); }
                70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(250, 204, 21, 0); }
                100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(250, 204, 21, 0); }
            }
            .globe-diplomacy-marker {
                background: rgba(250, 204, 21, 0.2);
                border: 1px solid #facc15;
                border-radius: 50%;
                padding: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .globe-diplomacy-core {
                background: #facc15;
                width: 8px;
                height: 8px;
                border-radius: 50%;
                animation: globe-pulse 2s infinite;
            }
        `;
        document.head.appendChild(style);
    }
};

interface GlobeTrackerProps {
    activeEvent: PulseEvent;
}

const GlobeTracker = memo(function GlobeTracker({ activeEvent }: GlobeTrackerProps) {
    const globeRef = useRef<any>(null);
    const [countries, setCountries] = useState({ features: EMPTY_ARRAY });

    useEffect(() => {
        fetch(GEOJSON_URL).then(res => res.json()).then(setCountries);
        injectStyles();
    }, []);

    // Lock camera to the Gulf region on mount and whenever event changes
    useEffect(() => {
        if (globeRef.current && activeEvent) {
            globeRef.current.pointOfView({
                lat: activeEvent.coordinates.lat,
                lng: activeEvent.coordinates.lng,
                altitude: 0.8
            }, 2000);
        }
    }, [activeEvent.id]);

    // Polygon styling - highlight involved nations in red or orange
    const getPolygonColor = useCallback((d: any) => {
        if (!activeEvent) return 'rgba(255,255,255,0.02)';
        const isoCode = d.properties['ISO3166-1-Alpha-3'];

        if (activeEvent.involvedCountries.includes(isoCode)) {
            if (activeEvent.category === "Kinetic Strike" || activeEvent.category === "War") {
                return `rgba(239, 68, 68, 0.4)`; // red
            }
            if (activeEvent.category === "Macroeconomic") {
                return `rgba(168, 85, 247, 0.4)`; // purple
            }
            return `rgba(251, 191, 36, 0.3)`; // amber for diplomacy/cyber
        }
        return 'rgba(255,255,255,0.02)';
    }, [activeEvent]);

    const getPolygonAltitude = useCallback((d: any) => {
        if (!activeEvent) return 0.01;
        const isTarget = activeEvent.involvedCountries.includes(d.properties['ISO3166-1-Alpha-3']);
        if (isTarget) {
            // Pulse macroeconomic strain highly
            if (activeEvent.action !== "none" && activeEvent.action?.type === "polygon") return 0.12;
            return 0.02;
        }
        return 0.01;
    }, [activeEvent]);

    // Animations Data
    const arcsData = useMemo(() => {
        if (activeEvent?.action !== "none" && activeEvent?.action?.type === "missile_arc") {
            return [{
                startLat: activeEvent.action !== "none" ? activeEvent.action.source?.lat : undefined,
                startLng: activeEvent.action !== "none" ? activeEvent.action.source?.lng : undefined,
                endLat: activeEvent.coordinates.lat,
                endLng: activeEvent.coordinates.lng,
                color: ['rgba(239, 68, 68, 0.2)', 'rgba(239, 68, 68, 1)'], // red gradient
                label: "Missile Strike"
            }];
        }
        return EMPTY_ARRAY;
    }, [activeEvent]);

    const ringsData = useMemo(() => {
        if (activeEvent) {
            // Base ripple radar for almost all active events except the pure polygon ones
            const colorMap: Record<string, string> = {
                'hex_bin': '#06b6d4',      // cyber cyan
                'html_element': '#facc15', // diplomacy yellow
                'missile_arc': '#ef4444',  // kinetic red
                'custom': '#ef4444',       // kinetic red
                'polygon': '#a855f7'       // purple macro
            };
            return [{
                lat: activeEvent.coordinates.lat,
                lng: activeEvent.coordinates.lng,
                maxR: activeEvent.category === "War" ? 8 : 4,
                propagationSpeed: activeEvent.category === "Cyber" ? 2 : 1.5,
                repeatPeriod: 1000,
                color: (activeEvent.action !== "none" && colorMap[activeEvent.action?.type || 'custom']) || '#ef4444'
            }];
        }
        return EMPTY_ARRAY;
    }, [activeEvent]);

    const customLayerData = useMemo(() => {
        if (activeEvent?.category === "Kinetic Strike" || activeEvent?.category === "War") {
            return [{
                lat: activeEvent.coordinates.lat,
                lng: activeEvent.coordinates.lng,
                size: 0.15,
                color: '#ef4444'
            }];
        }
        return EMPTY_ARRAY;
    }, [activeEvent]);

    const hexBinData = useMemo(() => {
        if (activeEvent?.action !== "none" && activeEvent?.action?.type === "hex_bin") {
            // Generate a small cluster around the target
            return Array.from({ length: 20 }).map(() => ({
                lat: activeEvent.coordinates.lat + (Math.random() - 0.5) * 2,
                lng: activeEvent.coordinates.lng + (Math.random() - 0.5) * 2,
                weight: Math.random()
            }));
        }
        return EMPTY_ARRAY;
    }, [activeEvent]);

    const htmlElementsData = useMemo(() => {
        if (activeEvent?.action !== "none" && activeEvent?.action?.type === "html_element") {
            return [{
                lat: activeEvent.coordinates.lat,
                lng: activeEvent.coordinates.lng
            }];
        }
        return EMPTY_ARRAY;
    }, [activeEvent]);

    const customThreeObject = useCallback((d: any) => {
        // Creates a stark, sharp cone for strikes pointing outwards
        const geometry = new THREE.ConeGeometry(d.size * 2, d.size * 6, 8);
        geometry.applyMatrix4(new THREE.Matrix4().makeRotationX(Math.PI / 2));
        const material = new THREE.MeshLambertMaterial({ color: d.color, transparent: true, opacity: 0.9 });
        return new THREE.Mesh(geometry, material);
    }, []);

    const htmlElement = useCallback(() => {
        const el = document.createElement('div');
        el.className = 'globe-diplomacy-marker';
        el.innerHTML = '<div class="globe-diplomacy-core"></div>';
        return el;
    }, []);

    const polygonSideColor = useCallback(() => 'rgba(0, 0, 0, 0.4)', []);
    const polygonStrokeColor = useCallback(() => '#222', []);

    return (
        <Globe
            ref={globeRef}
            globeImageUrl="https://unpkg.com/three-globe/example/img/earth-dark.jpg"
            bumpImageUrl="https://unpkg.com/three-globe/example/img/earth-topology.png"
            backgroundImageUrl="https://unpkg.com/three-globe/example/img/night-sky.png"

            // Polygons
            polygonsData={countries.features}
            polygonAltitude={getPolygonAltitude}
            polygonCapColor={getPolygonColor}
            polygonSideColor={polygonSideColor}
            polygonStrokeColor={polygonStrokeColor}

            // Animations - Arcs & Rings
            arcsData={arcsData}
            arcColor="color"
            arcDashLength={0.4}
            arcDashGap={0.2}
            arcDashAnimateTime={1500}
            arcAltitude={0.3}
            arcStroke={1.5}

            ringsData={ringsData}
            ringColor="color"
            ringMaxRadius="maxR"
            ringPropagationSpeed="propagationSpeed"
            ringRepeatPeriod="repeatPeriod"

            // Animations - Advanced 3D (Custom, Hex, HTML)
            customLayerData={customLayerData}
            customThreeObject={customThreeObject}

            hexBinPointsData={hexBinData}
            hexBinPointWeight="weight"
            hexAltitude={useCallback((d: any) => d.sumWeight * 0.1, [])}
            hexBinResolution={4}
            hexTopColor={useCallback(() => '#06b6d4', [])}
            hexSideColor={useCallback(() => 'rgba(6, 182, 212, 0.2)', [])}

            htmlElementsData={htmlElementsData}
            htmlElement={htmlElement}

            // Base Config
            animateIn={true}
        />
    );
});

export default GlobeTracker;
