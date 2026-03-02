import json
import random
import uuid
from datetime import datetime, timedelta

def generate_data():
    start_date = datetime(2026, 1, 1)
    end_date = datetime(2026, 3, 1, 23, 59, 59)
    
    events = []
    markets = []
    
    current_brent = 78.50
    current_gold = 2050.00
    
    # Story beats
    # Jan 1-15: Rising tension, diplomacy stalling
    # Jan 15-31: Iran protests, proxy attacks in Red Sea
    # Feb 1-15: US buildup in Gulf, Israel threats
    # Feb 20: Initial skirmishes / targeted strikes
    # Feb 28: Major Operation Epic Fury
    # Mar 1: Iranian retaliation
    
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        
        # Determine macro impacts for the day
        brent_change = random.uniform(-0.5, 0.6)
        gold_change = random.uniform(-5.0, 6.0)
        
        # Inject key narrative events
        daily_events = []
        
        if date_str == "2026-01-05":
            daily_events.append({
                "title": "US Issues Stern Warning on Uranium Enrichment",
                "desc": "The White House sets a strict deadline for Iran to halt 60% uranium enrichment, warning of 'severe consequences' if ignored by the end of January.",
                "cat": "Diplomacy",
                "inv": ["USA", "IRN"],
                "impact": "Markets mostly shrug off standard diplomatic posturing, though gold ticks up slightly.",
                "coords": {"lat": 35.6892, "lng": 51.3890}, # Tehran
                "action": "none"
            })
            gold_change += 10
            
        elif date_str == "2026-01-18":
             daily_events.append({
                "title": "Houthi Red Sea Strike Hits Tanker",
                "desc": "A commercial oil tanker is struck by a suspected Iranian-supplied drone in the Red Sea, temporarily disrupting shipping lanes.",
                "cat": "Kinetic Strike",
                "inv": ["IRN", "USA"],
                "impact": "Brent crude spikes 2% on localized supply chain fears.",
                "coords": {"lat": 15.3, "lng": 41.5},
                "action": {"type": "impact_ripple", "target": "15.3,41.5", "color": "var(--accent-red)"}
            })
             brent_change += 1.8
             
        elif date_str == "2026-02-05":
            daily_events.append({
                "title": "Massive US Naval Buildup in Persian Gulf",
                "desc": "Satellite imagery confirms the arrival of two US carrier strike groups in the Gulf, marking the largest deployment since 2003.",
                "cat": "War",
                "inv": ["USA", "IRN"],
                "impact": "Oil markets price in a rising risk premium as regional war seems increasingly likely.",
                "coords": {"lat": 26.2, "lng": 54.8},
                "action": "none"
            })
            brent_change += 2.5
            gold_change += 20
            
        elif date_str == "2026-02-20":
            daily_events.append({
                "title": "US Intelligence Warns of Imminent Gulf Threats",
                "desc": "Declassified intelligence reports suggest heightened movements of drone and missile batteries along the Iranian coast, targeting key shipping lanes.",
                "cat": "Diplomacy",
                "inv": ["USA", "IRN"],
                "impact": "Brent Crude rises 1.5% to $82/bbl on supply fears.",
                "coords": {"lat": 26.5, "lng": 56.2}, # Strait of Hormuz
                "action": "none"
            })
            brent_change += 1.2
            
            # Additional Feb 20 event
            current_date = current_date.replace(hour=18, minute=30)
            daily_events.append({
                 "title": "Cyberattack Cripples Kuwaiti Oil Infrastructure",
                 "desc": "State-sponsored hacking groups, suspected to be Iranian affiliates, temporarily disable crucial oil terminal systems in Kuwait.",
                 "cat": "Cyber",
                 "inv": ["IRN", "KWT"],
                 "impact": "Fears of broader cyber warfare push gold to $2300.",
                 "coords": {"lat": 29.3, "lng": 47.9},
                 "action": {"type": "impact_ripple", "target": "29.3,47.9", "color": "var(--accent-blue)"}
            })
            gold_change += 15
            current_date = current_date.replace(hour=0, minute=0)

        elif date_str == "2026-02-28":
            # Operation Epic Fury
            current_date = current_date.replace(hour=2, minute=15)
            daily_events.append({
                 "title": "Operation Epic Fury Commences",
                 "desc": "A major joint military operation led by the US and Israel begins, targeting Iranian nuclear facilities and missile launch sites.",
                 "cat": "War",
                 "inv": ["USA", "ISR", "IRN"],
                 "impact": "Global markets shock. Brent crude surges past $90, Gold hits record highs above $2400.",
                 "coords": {"lat": 33.86, "lng": 49.33}, # Arak heavy water
                 "action": {"type": "missile_arc", "source": {"lat": 31.7, "lng": 35.2}, "target": "33.86,49.33", "color": "var(--accent-red)"}
            })
            brent_change += 8.0
            gold_change += 80.0
            
            current_date = current_date.replace(hour=14, minute=0)
            daily_events.append({
                 "title": "Major Iranian Leadership Causalities Reported",
                 "desc": "Unverified reports from regional news agencies suggest key Iranian military and political leaders were killed in the overwhelming precision strikes.",
                 "cat": "Kinetic Strike",
                 "inv": ["USA", "ISR", "IRN"],
                 "impact": "Significant geopolitical destabilization. Oil trading halts briefly on ICE.",
                 "coords": {"lat": 35.7, "lng": 51.4}, # Tehran
                 "action": {"type": "impact_ripple", "target": "35.7,51.4", "color": "var(--accent-red)"}
            })
            current_date = current_date.replace(hour=0, minute=0)

        elif date_str == "2026-03-01":
            current_date = current_date.replace(hour=4, minute=45)
            daily_events.append({
                 "title": "Iran Retaliates: Missiles Hit Gulf Bases",
                 "desc": "In swift retaliation, Iran launches barrages of ballistic missiles targeting US military installations in Bahrain, Qatar, and the UAE.",
                 "cat": "Kinetic Strike",
                 "inv": ["IRN", "USA", "ARE", "QAT", "BHR"],
                 "impact": "Unprecedented regional war fears. Strait of Hormuz effectively closed to commercial shipping.",
                 "coords": {"lat": 26.06, "lng": 50.55}, # Bahrain
                 "action": {"type": "missile_arc", "source": {"lat": 29.6, "lng": 52.5}, "target": "26.06,50.55", "color": "var(--accent-red)"}
            })
            brent_change += 5.0
            gold_change += 25.0
            current_date = current_date.replace(hour=0, minute=0)

        # Apply market changes
        current_brent += brent_change
        current_gold += gold_change
        
        markets.append({
            "time": date_str,
            "brent": round(current_brent, 2),
            "gold": round(current_gold, 2)
        })
        
        for de in daily_events:
            event_date = current_date.replace(hour=random.randint(8,20), minute=random.randint(0,59)) if "00:00:00" in str(current_date) else current_date
            
            # Action formatting
            act = de["action"]
            if type(act) == dict and act.get("type") == "missile_arc":
                act_obj = act
            elif type(act) == dict and act.get("type") == "impact_ripple":
                act_obj = act
            else:
                act_obj = "none"

            events.append({
                "id": str(uuid.uuid4()),
                "date": event_date.isoformat() + "Z",
                "title": de["title"],
                "description": de["desc"],
                "category": de["cat"],
                "involvedCountries": de["inv"],
                "impact": de["impact"],
                "sources": [
                    {"name": "Reuters", "url": "#", "type": "verified"},
                    {"name": "Bloomberg", "url": "#", "type": "verified"}
                ],
                "tags": [de["cat"], "Middle East", "Oil"],
                "coordinates": de["coords"],
                "action": act_obj
            })
            
        current_date += timedelta(days=1)
        
    final_payload = {
        "events": events,
        "markets": markets
    }
    
    with open("src/data/events.json", "w") as f:
        json.dump(final_payload, f, indent=2)

if __name__ == "__main__":
    generate_data()
    print("Data successfully generated.")
