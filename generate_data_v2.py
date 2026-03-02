import json
import random
import uuid
from datetime import datetime, timedelta

def create_event(date_obj, title, desc, cat, inv, impact, lat, lng, action_type="none", target=None, source_coords=None):
    # Determine act based on new categories
    if action_type == "missile_arc":
        act = {"type": "missile_arc", "source": source_coords, "target": f"{lat},{lng}", "color": "var(--accent-red)"}
    else:
        if cat in ["Kinetic Strike", "War"]:
            act = {"type": "custom", "target": f"{lat},{lng}", "color": "var(--accent-red)"}
        elif cat == "Cyber":
            act = {"type": "hex_bin", "target": f"{lat},{lng}", "color": "var(--accent-blue)"}
        elif cat == "Diplomacy":
            act = {"type": "html_element", "target": f"{lat},{lng}", "color": "#facc15"} # Yellow
        elif cat == "Macroeconomic":
            act = {"type": "polygon", "target": f"{lat},{lng}", "color": "#a855f7"} # Purple
        else:
            act = {"type": "point", "target": f"{lat},{lng}", "color": "#f97316"} # Orange
        
    return {
        "id": str(uuid.uuid4()),
        "date": date_obj.isoformat() + "+05:30", # Ensure timezone format matches
        "title": title,
        "description": desc,
        "category": cat,
        "involvedCountries": inv,
        "impact": impact,
        "sources": [
            {"name": "Reuters", "url": "#", "type": "verified"},
            {"name": "Bloomberg", "url": "#", "type": "verified"}
        ],
        "tags": [cat, "Middle East", "Conflict 2026"],
        "coordinates": {"lat": lat, "lng": lng},
        "action": act
    }

def generate_data():
    start_date = datetime(2026, 1, 1)
    end_date = datetime(2026, 3, 1, 23, 59, 59)
    
    events = []
    
    # JAN 1 - FEB 27 (Gradual build up, 15 events)
    events.append(create_event(datetime(2026, 1, 5, 10, 0), "US Issues Stern Warning on Uranium Enrichment", "The White House sets a strict deadline for Iran to halt 60% uranium enrichment.", "Diplomacy", ["USA", "IRN"], "Gold ticks up slightly.", 35.6892, 51.3890))
    events.append(create_event(datetime(2026, 1, 9, 14, 30), "Protests Erupt in Tehran", "Large-scale anti-government protests break out over economic conditions.", "Diplomacy", ["IRN"], "Internal destabilization noted by markets.", 35.6892, 51.3890))
    events.append(create_event(datetime(2026, 1, 14, 8, 15), "Israel Briefs White House on Strike Plans", "Leaked intelligence suggests PM Netanyahu briefed the US on potential unilateral strike packages.", "Diplomacy", ["ISR", "USA"], "Oil climbs 1%.", 31.7683, 35.2137))
    events.append(create_event(datetime(2026, 1, 18, 11, 45), "Houthi Drone Strikes Red Sea Tanker", "A commercial oil tanker is struck by a suspected Iranian-supplied drone.", "Kinetic Strike", ["IRN", "YEM"], "Brent crude spikes 2%.", 15.3, 41.5, "impact_ripple"))
    events.append(create_event(datetime(2026, 1, 23, 16, 20), "Oman Mediation Talks Collapse", "Indirect talks mediated by Oman between US and Iranian diplomats fail to produce a breakthrough.", "Diplomacy", ["USA", "IRN", "OMN"], "Market pessimism rises.", 23.5859, 58.4059))
    events.append(create_event(datetime(2026, 2, 2, 9, 0), "US Increases Sanctions on Iranian Drone Manufacturers", "Treasury Dept blacklists 15 shell companies supplying drone parts.", "Macroeconomic", ["USA", "IRN"], "Minor currency fluctuations.", 38.9072, -77.0369))
    events.append(create_event(datetime(2026, 2, 5, 13, 0), "Massive US Naval Buildup", "Satellite imagery confirms two US carrier strike groups in the Gulf.", "War", ["USA", "IRN"], "Oil markets price in war premium.", 26.2, 54.8))
    events.append(create_event(datetime(2026, 2, 9, 21, 15), "Cyberattack on Israeli Water Infrastructure", "Iranian-linked hackers attempt to breach municipal water controls in Tel Aviv.", "Cyber", ["IRN", "ISR"], "Heightened alert protocols initiated.", 32.0853, 34.7818, "impact_ripple"))
    events.append(create_event(datetime(2026, 2, 14, 18, 50), "Israel Intercepts Drone Swarm from Syria", "Iron Dome and David's Sling activate extensively in the Golan Heights.", "Kinetic Strike", ["ISR", "SYR", "IRN"], "Gold surges past $2100.", 33.0, 35.8, "impact_ripple"))
    events.append(create_event(datetime(2026, 2, 18, 7, 30), "UN Secretary General Warns of Grave Threat", "António Guterres calls for immediate cessation of hostilities.", "Diplomacy", ["UN", "USA", "IRN", "ISR"], "Diplomatic efforts peak.", 40.7484, -73.9857))
    events.append(create_event(datetime(2026, 2, 20, 10, 0), "US Intelligence Warns of Imminent Gulf Threats", "Declassified reports show drone battery movements.", "Diplomacy", ["USA", "IRN"], "Brent hits $82/bbl.", 26.5, 56.2))
    events.append(create_event(datetime(2026, 2, 21, 14, 20), "Cyberattack Cripples Kuwaiti Oil Infrastructure", "Operations paused at major terminal.", "Cyber", ["IRN", "KWT"], "Supply chain fears mount.", 29.3, 47.9, "impact_ripple"))
    events.append(create_event(datetime(2026, 2, 24, 19, 45), "US Embassies in Middle East Begin Evacuations", "Non-essential staff ordered out of Iraq, Lebanon, and Bahrain.", "Diplomacy", ["USA", "IRQ", "LBN", "BHR"], "Panic trading begins.", 33.3128, 44.3615))
    events.append(create_event(datetime(2026, 2, 26, 8, 0), "Iran Threatens to Close Strait of Hormuz", "IRGC naval commander states the strait will be closed if Iranian oil exports are targeted.", "War", ["IRN", "USA"], "Brent crude skyrockets 4%.", 26.56, 56.25))
    events.append(create_event(datetime(2026, 2, 27, 23, 30), "Unprecedented Communications Blackout in Iran", "Internet and cellphone networks go dark across major Iranian cities.", "Cyber", ["USA", "IRN"], "Imminent strike expected.", 35.6892, 51.3890, "impact_ripple"))

    # FEB 28 - THE OPERATION (20 events, high density)
    base_date = datetime(2026, 2, 28)
    events.append(create_event(base_date.replace(hour=2, minute=15), "Operation Epic Fury Commences", "Joint US-Israeli military operation begins.", "War", ["USA", "ISR", "IRN"], "Global markets in shock.", 33.86, 49.33, "missile_arc", source_coords={"lat": 31.7, "lng": 35.2}))
    events.append(create_event(base_date.replace(hour=2, minute=45), "Strikes on Natanz Enrichment Facility", "Heavy bunker-buster munitions deployed against underground nuclear sites.", "Kinetic Strike", ["ISR", "IRN"], "Gold hits $2300.", 33.72, 51.72, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=3, minute=10), "Fordow Fuel Enrichment Plant Highly Damaged", "Second wave of strikes hits deep mountain facilities.", "Kinetic Strike", ["USA", "IRN"], "Brent crosses $90.", 34.88, 50.99, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=3, minute=50), "Iranian Air Defenses Suppressed", "US electronic warfare planes blind coastal radar systems.", "Cyber", ["USA", "IRN"], "Airspace dominance secured.", 35.0, 50.0))
    events.append(create_event(base_date.replace(hour=4, minute=30), "Bandar Abbas Naval Base Struck", "Tomahawk cruise missiles destroy speedboats and submarine pens.", "Kinetic Strike", ["USA", "IRN"], "Naval threat neutralized.", 27.18, 56.27, "missile_arc", source_coords={"lat": 26.2, "lng": 54.8}))
    events.append(create_event(base_date.replace(hour=5, minute=15), "Explosions Near Isfahan Military Complex", "Drone manufacturing hubs heavily hit.", "Kinetic Strike", ["ISR", "IRN"], "Supply lines severed.", 32.65, 51.66, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=6, minute=0), "China Condemns Violation of Sovereignty", "Beijing issues strong statement against unprovoked attacks.", "Diplomacy", ["CHN", "USA", "ISR"], "Yuan dips.", 39.90, 116.40))
    events.append(create_event(base_date.replace(hour=7, minute=20), "Parchin Military Complex Bombarded", "Facilities linked to weaponization research destroyed.", "Kinetic Strike", ["USA", "IRN"], "Nuclear program degraded.", 35.53, 51.77, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=8, minute=45), "Global Air Travel Diverted", "Commercial flights rerouted entirely away from Middle East airspace.", "Macroeconomic", ["Global"], "Airlines stocks plummet.", 25.27, 55.33))
    events.append(create_event(base_date.replace(hour=10, minute=10), "Russian Statements of Support for Iran", "Moscow calls an emergency UN Security Council meeting.", "Diplomacy", ["RUS", "IRN"], "Geopolitical fracture deepens.", 55.75, 37.61))
    events.append(create_event(base_date.replace(hour=11, minute=30), "IRGC Headquarters in Tehran Decimated", "Precision strikes target command and control centers in the capital.", "Kinetic Strike", ["USA", "IRN"], "Leadership communications severed.", 35.7, 51.4, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=12, minute=45), "US Pentagon Press Briefing", "DOD confirms massive degradation of Iranian offensive capabilities.", "Diplomacy", ["USA"], "Markets stabilize slightly.", 38.87, -77.05))
    events.append(create_event(base_date.replace(hour=14, minute=0), "Major Iranian Leadership Causalities Reported", "Unverified reports suggest Ayatollah Ali Khamenei assassinated.", "Kinetic Strike", ["USA", "ISR", "IRN"], "Oil trading halts briefly.", 35.7, 51.4, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=15, minute=20), "Secondary Explosions at Missile Silos", "Kermanshah ballistic missile bases continue burning.", "Kinetic Strike", ["USA", "IRN"], "Retaliatory capability reduced.", 34.31, 47.06, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=17, minute=15), "Saudi Arabia Closes Airspace", "Riyadh braces for spillover violence.", "Macroeconomic", ["SAU"], "Oil stays elevated.", 24.71, 46.67))
    events.append(create_event(base_date.replace(hour=18, minute=40), "Cyber Retaliation on US Financial Sector", "DDoS attacks temporarily slow Wall Street banking portals.", "Cyber", ["IRN", "USA"], "VIX spikes 30%.", 40.71, -74.00, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=20, minute=0), "Operation Roaring Lion Concludes Phase 1", "Israeli officials declare primary nuclear targets eliminated.", "War", ["ISR"], "Regional blackout continues.", 31.76, 35.21))
    events.append(create_event(base_date.replace(hour=21, minute=30), "Hezbollah Mobilizes on Northern Border", "Lebanese militant front begins heavy artillery fire into Northern Israel.", "Kinetic Strike", ["LBN", "ISR"], "Two-front war begins.", 33.27, 35.5, "missile_arc", source_coords={"lat": 33.8, "lng": 35.5}))
    events.append(create_event(base_date.replace(hour=22, minute=45), "US Embassies in Europe High Alert", "Intelligence suggests sleeper cell activations globally.", "War", ["USA", "EU"], "Global security tightened.", 50.85, 4.35))
    events.append(create_event(base_date.replace(hour=23, minute=50), "Iran TV Broadcasts Surviving Commander", "IRGC general promises 'earth-shattering revenge' before dawn.", "Diplomacy", ["IRN", "USA", "ISR"], "Bracing for impact.", 35.68, 51.38))

    # MAR 1 - RETALIATION (15+ events, extreme density including late evening)
    base_date = datetime(2026, 3, 1)
    events.append(create_event(base_date.replace(hour=1, minute=10), "First Wave: Ballistic Missiles Launched", "Radar detects multiple launches from deep underground silos in Iran.", "War", ["IRN", "USA"], "Sirens across the Gulf.", 32.0, 54.0))
    events.append(create_event(base_date.replace(hour=1, minute=45), "Missiles Strike Tel Aviv Outskirts", "A few missiles penetrate the Arrow defense grid, causing structure damage.", "Kinetic Strike", ["IRN", "ISR"], "Gold blasts past $2400.", 32.08, 34.78, "missile_arc", source_coords={"lat": 34.31, "lng": 47.06}))
    events.append(create_event(base_date.replace(hour=2, minute=30), "Al Udeid Air Base Qatar Attacked", "Largest US base in region hit by drone swarms.", "Kinetic Strike", ["IRN", "USA", "QAT"], "Base lockdown. Minor damage.", 25.11, 51.31, "missile_arc", source_coords={"lat": 27.18, "lng": 56.27}))
    events.append(create_event(base_date.replace(hour=3, minute=15), "US Navy Destroyer Engages Threat in Gulf", "USS Thomas Hudner shoots down 4 anti-ship cruise missiles.", "Kinetic Strike", ["USA", "IRN"], "Naval battle commenced.", 26.0, 55.0, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=4, minute=45), "Missiles Hit Gulf Bases in Bahrain and UAE", "Heavy barrage targets US 5th Fleet headquarters in Manama and Al Dhafra AB.", "Kinetic Strike", ["IRN", "USA", "BHR", "ARE"], "Significant casualties feared.", 26.06, 50.55, "missile_arc", source_coords={"lat": 29.6, "lng": 52.5}))
    events.append(create_event(base_date.replace(hour=6, minute=20), "Pentagon Confirms Initial Causalities", "3 US Service members confirmed KIA, 5 severely injured.", "War", ["USA"], "National mourning and anger.", 38.87, -77.05))
    events.append(create_event(base_date.replace(hour=8, minute=0), "Emergency POTUS Address to Nation", "President vows swift, disproportionate response if attacks continue.", "Diplomacy", ["USA"], "Markets extremely volatile.", 38.89, -77.03))
    events.append(create_event(base_date.replace(hour=9, minute=30), "Global Markets React", "Asian markets crash by 6%. European markets open sharply lower.", "Macroeconomic", ["Global"], "Flight to safety in US Treasuries and Gold.", 35.67, 139.75))
    events.append(create_event(base_date.replace(hour=10, minute=45), "Missile Strike on Saudi Oil Installation", "Abqaiq facility targeted again, multiple fires reported.", "Kinetic Strike", ["IRN", "SAU"], "Brent touches $100/bbl.", 25.93, 49.67, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=12, minute=15), "Israel Strikes Beirut Suburbs", "Retaliation against Hezbollah command centers.", "Kinetic Strike", ["ISR", "LBN"], "Massive civilian displacement.", 33.88, 35.49, "missile_arc", source_coords={"lat": 32.8, "lng": 34.9}))
    events.append(create_event(base_date.replace(hour=13, minute=53), "Houthi Missile Intercepted Over Eilat", "Israel's Arrow-3 intercepts surface-to-surface missile.", "Kinetic Strike", ["YEM", "ISR"], "Air defense strains.", 29.55, 34.95, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=15, minute=30), "Pope Calls for Halt to Spiral of Violence", "Vatican issues desperate plea for peace and negotiations.", "Diplomacy", ["VAT", "Global"], "Moral appeal gains traction.", 41.90, 12.45))
    events.append(create_event(base_date.replace(hour=17, minute=10), "Strait of Hormuz Effectively Closed", "Burning tankers block shipping lanes. Insurance premiums halt traffic.", "Macroeconomic", ["Global"], "Largest energy shock since 1970s.", 26.56, 56.25))
    events.append(create_event(base_date.replace(hour=19, minute=0), "US B-2 Bombers Deployed", "Stealth bombers seen leaving Diego Garcia, heading towards Iran.", "War", ["USA", "IRN"], "Escalation to massive retaliation expected.", -7.31, 72.41, "missile_arc", source_coords={"lat": -7.3, "lng": 72.4}))
    events.append(create_event(base_date.replace(hour=21, minute=45), "Massive Blackout in Northern Israel", "Suspected combined cyber and kinetic attack knocks out power grid.", "Cyber", ["IRN", "LBN", "ISR"], "Civilians ordered to bunkers.", 32.8, 35.0, "impact_ripple"))
    events.append(create_event(base_date.replace(hour=23, minute=15), "UN Security Council Deadlocks", "US vetoes ceasefire resolution demanding complete Israeli withdrawal.", "Diplomacy", ["UN", "USA", "RUS", "CHN"], "Diplomatic failure complete.", 40.75, -73.98))
    events.append(create_event(base_date.replace(hour=23, minute=55), "Second Wave Warnings Sirens Sound in UAE", "Incoming missile alerts trigger mass panic in Dubai and Abu Dhabi.", "War", ["IRN", "ARE"], "Chaos ensues into midnight.", 25.20, 55.27))

    # Generate daily market data for 60 days
    brent_actuals = {
        "2026-01-02": 60.75, "2026-01-05": 61.76, "2026-01-06": 60.70,
        "2026-01-07": 59.96, "2026-01-08": 61.99, "2026-01-09": 63.34,
        "2026-01-12": 63.87, "2026-01-13": 65.47, "2026-01-14": 66.52,
        "2026-01-15": 63.76, "2026-01-16": 64.13, "2026-01-20": 64.92,
        "2026-01-21": 65.24, "2026-01-22": 64.06, "2026-01-23": 65.88,
        "2026-01-26": 65.59, "2026-01-27": 67.57, "2026-01-28": 68.40,
        "2026-01-29": 70.71, "2026-01-30": 70.69, "2026-02-02": 66.30,
        "2026-02-03": 67.33, "2026-02-04": 69.46, "2026-02-05": 67.55,
        "2026-02-06": 68.05, "2026-02-09": 69.04, "2026-02-10": 68.80,
        "2026-02-11": 69.40, "2026-02-12": 67.52, "2026-02-13": 67.75,
        "2026-02-16": 67.97, "2026-02-17": 66.87, "2026-02-18": 69.77,
        "2026-02-19": 71.27, "2026-02-20": 71.30, "2026-02-23": 71.49,
        "2026-02-24": 70.77, "2026-02-25": 70.85, "2026-02-26": 70.75,
        "2026-02-27": 72.48, "2026-03-01": 78.36
    }

    def get_brent_price(target_date_str):
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        for i in range(100):
            check_date = target_date + timedelta(days=i)
            check_str = check_date.strftime("%Y-%m-%d")
            if check_str in brent_actuals:
                return brent_actuals[check_str]
        return list(brent_actuals.values())[-1]

    gold_actuals = {
        "2026-01-01": 4321.48, "2026-01-02": 4329.60, "2026-01-05": 4451.50,
        "2026-01-06": 4496.10, "2026-01-07": 4462.50, "2026-01-08": 4460.70,
        "2026-01-09": 4500.90, "2026-01-12": 4614.70, "2026-01-13": 4599.10,
        "2026-01-14": 4635.70, "2026-01-15": 4623.70, "2026-01-16": 4595.40,
        "2026-01-20": 4765.80, "2026-01-21": 4837.50, "2026-01-22": 4913.40,
        "2026-01-23": 4979.70, "2026-01-26": 5122.30, "2026-01-27": 5120.60,
        "2026-01-28": 5340.20, "2026-01-29": 5354.80, "2026-01-30": 4745.10,
        "2026-02-02": 4652.60, "2026-02-03": 4935.00, "2026-02-04": 4950.80,
        "2026-02-05": 4889.50, "2026-02-06": 4979.80, "2026-02-09": 5079.40,
        "2026-02-10": 5031.00, "2026-02-11": 5098.50, "2026-02-12": 4948.40,
        "2026-02-13": 5046.30, "2026-02-17": 4905.90, "2026-02-18": 5009.50,
        "2026-02-19": 4997.40, "2026-02-20": 5080.90, "2026-02-23": 5207.50,
        "2026-02-24": 5157.80, "2026-02-25": 5208.00, "2026-02-26": 5194.20,
        "2026-02-27": 5247.90, "2026-02-28": 5282.00, "2026-03-01": 5319.50
    }

    def get_gold_price(target_date_str):
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        for i in range(100):
            check_date = target_date + timedelta(days=i)
            check_str = check_date.strftime("%Y-%m-%d")
            if check_str in gold_actuals:
                return gold_actuals[check_str]
        return list(gold_actuals.values())[-1]

    markets = []
    
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        
        brent_price = get_brent_price(date_str)
        gold_price = get_gold_price(date_str)
        
        markets.append({
            "time": date_str,
            "brent": brent_price,
            "gold": gold_price
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
    print("Comprehensive Data V2 successfully generated.")
