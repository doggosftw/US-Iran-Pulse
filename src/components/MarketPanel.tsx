import { useMemo } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, ReferenceDot } from 'recharts';
import type { MarketData } from '../App';

interface MarketPanelProps {
    markets: MarketData[];
    currentDateStr: string; // The time of the active event
}

export default function MarketPanel({ markets, currentDateStr }: MarketPanelProps) {

    // Find the closest market data point to the current event date
    const currentIndex = useMemo(() => {
        const eventTime = new Date(currentDateStr).getTime();

        // Simple closest match search
        let closestIdx = 0;
        let minDiff = Infinity;

        markets.forEach((m, idx) => {
            const diff = Math.abs(new Date(m.time).getTime() - eventTime);
            if (diff < minDiff) {
                minDiff = diff;
                closestIdx = idx;
            }
        });

        return closestIdx;
    }, [markets, currentDateStr]);

    const currentMarket = markets[currentIndex];

    // Dynamic starting date label
    const startObj = new Date(markets[0].time);
    const startStr = startObj.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });

    // Custom generic tooltip for Recharts to handle dark mode
    const CustomTooltip = ({ active, payload }: any) => {
        if (active && payload && payload.length) {
            return (
                <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.9)', padding: '8px 12px', border: '1px solid var(--glass-border)', borderRadius: '6px', fontSize: '0.75rem' }}>
                    <p style={{ color: '#94a3b8', marginBottom: '4px' }}>
                        {new Date(payload[0].payload.time).toLocaleDateString('en-US', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })}
                    </p>
                    <p style={{ color: payload[0].color, fontWeight: 'bold' }}>
                        {payload[0].name}: ${payload[0].value}
                    </p>
                </div>
            );
        }
        return null;
    };

    return (
        <div className="market-panel-inner animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>

            {/* BRENT CRUDE OIL */}
            <div>
                <div style={{ display: 'flex', flexDirection: 'column', marginBottom: '8px' }}>
                    <span style={{ fontSize: '0.8rem', color: '#94a3b8', textTransform: 'uppercase', fontWeight: 600 }}>Brent Crude</span>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginTop: '4px' }}>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <span style={{ fontSize: '0.7rem', color: '#64748b' }}>Start ({startStr})</span>
                            <span style={{ fontSize: '0.9rem', color: '#94a3b8', fontWeight: 500 }}>
                                ${markets[0]?.brent.toFixed(2)}
                            </span>
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end' }}>
                            <span style={{ fontSize: '0.7rem', color: '#64748b' }}>Current selected</span>
                            <span style={{ fontSize: '1.2rem', color: 'var(--accent-red)', fontWeight: 700 }}>
                                ${currentMarket?.brent.toFixed(2)}
                            </span>
                        </div>
                    </div>
                </div>
                <div style={{ height: '60px', width: '100%' }}>
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={markets}>
                            <XAxis dataKey="time" hide />
                            <YAxis domain={['dataMin - 2', 'dataMax + 2']} hide />
                            <Tooltip content={<CustomTooltip />} />
                            <Line
                                type="monotone"
                                dataKey="brent"
                                name="Brent Crude"
                                stroke="var(--accent-red)"
                                strokeWidth={2}
                                dot={false}
                                isAnimationActive={false} // Disable to make scrubbing fast
                            />
                            {currentMarket && (
                                <ReferenceDot x={currentMarket.time} y={currentMarket.brent} r={4} fill="var(--accent-red)" stroke="white" />
                            )}
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>

            <hr style={{ border: 'none', borderTop: '1px solid var(--glass-border)' }} />

            {/* GOLD */}
            <div>
                <div style={{ display: 'flex', flexDirection: 'column', marginBottom: '8px' }}>
                    <span style={{ fontSize: '0.8rem', color: '#94a3b8', textTransform: 'uppercase', fontWeight: 600 }}>Gold (Oz)</span>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginTop: '4px' }}>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <span style={{ fontSize: '0.7rem', color: '#64748b' }}>Start ({startStr})</span>
                            <span style={{ fontSize: '0.9rem', color: '#94a3b8', fontWeight: 500 }}>
                                ${markets[0]?.gold.toFixed(2)}
                            </span>
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end' }}>
                            <span style={{ fontSize: '0.7rem', color: '#64748b' }}>Current selected</span>
                            <span style={{ fontSize: '1.2rem', color: 'var(--accent-gold)', fontWeight: 700 }}>
                                ${currentMarket?.gold.toFixed(2)}
                            </span>
                        </div>
                    </div>
                </div>
                <div style={{ height: '60px', width: '100%' }}>
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={markets}>
                            <XAxis dataKey="time" hide />
                            <YAxis domain={['dataMin - 20', 'dataMax + 20']} hide />
                            <Tooltip content={<CustomTooltip />} />
                            <Line
                                type="monotone"
                                dataKey="gold"
                                name="Gold"
                                stroke="var(--accent-gold)"
                                strokeWidth={2}
                                dot={false}
                                isAnimationActive={false}
                            />
                            {currentMarket && (
                                <ReferenceDot x={currentMarket.time} y={currentMarket.gold} r={4} fill="var(--accent-gold)" stroke="white" />
                            )}
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>

        </div>
    );
}
