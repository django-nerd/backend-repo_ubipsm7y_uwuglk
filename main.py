import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Orthodox + Oriental Orthodox Overview API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Backend!"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend API!"}

@app.get("/test")
def test_database():
    """Test endpoint to check if database is available and accessible"""
    response = {
        "backend": "✅ Running",
        "database": "❌ Not Available",
        "database_url": None,
        "database_name": None,
        "connection_status": "Not Connected",
        "collections": []
    }
    
    try:
        # Try to import database module
        from database import db
        
        if db is not None:
            response["database"] = "✅ Available"
            response["database_url"] = "✅ Configured"
            response["database_name"] = db.name if hasattr(db, 'name') else "✅ Connected"
            response["connection_status"] = "Connected"
            
            # Try to list collections to verify connectivity
            try:
                collections = db.list_collection_names()
                response["collections"] = collections[:10]  # Show first 10 collections
                response["database"] = "✅ Connected & Working"
            except Exception as e:
                response["database"] = f"⚠️  Connected but Error: {str(e)[:50]}"
        else:
            response["database"] = "⚠️  Available but not initialized"
            
    except ImportError:
        response["database"] = "❌ Database module not found (run enable-database first)"
    except Exception as e:
        response["database"] = f"❌ Error: {str(e)[:50]}"
    
    # Check environment variables
    import os
    response["database_url"] = "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set"
    response["database_name"] = "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set"
    
    return response

# --------- Content for the Orthodox + Oriental Orthodox Overview ----------

def build_overview():
    return {
        "title": "Eastern Orthodox and Oriental Orthodox — Teaching Overview",
        "audiences": {
            "eastern_orthodox": ["Greek", "Russian", "Serbian", "Romanian", "Georgian", "Antiochian"],
            "oriental_orthodox": ["Coptic", "Syriac", "Armenian", "Ethiopian (Tewahedo)", "Eritrean", "Malankara (Indian)"]
        },
        "shared_core": [
            "Trinity: One God in three Persons; full divinity of the Son and Spirit.",
            "Christ: Truly God and truly man; Mary as Theotokos; crucified, risen, and coming again.",
            "Scripture and Holy Tradition together; Fathers, liturgy, and councils have real authority.",
            "Sacramental life: baptism, chrismation, Eucharist, confession, ordination, marriage, unction.",
            "Apostolic succession and episcopacy; bishops, presbyters, deacons.",
            "Worship and piety: liturgical prayer, fasting, veneration of saints and relics, monasticism, icons.",
            "Moral/spiritual vision: deification (theosis) and synergy of divine grace and human freedom."
        ],
        "split_history": {
            "century": 5,
            "trigger": "Reception of the Council of Chalcedon (AD 451)",
            "core_issue": "How to speak about Christ’s divinity and humanity united in one Person.",
            "eo_position": "Affirms Chalcedon: one Person in two natures; later councils affirm two wills/energies.",
            "oo_position": "Cyrillian miaphysite formula: one incarnate nature of the Word, without confusion or separation; rejects Chalcedon as misleading."
        },
        "councils_recognized": {
            "eastern_orthodox": "Seven Ecumenical Councils (Nicaea I to Nicaea II)",
            "oriental_orthodox": "First three Ecumenical Councils (Nicaea I, Constantinople I, Ephesus) plus local synods"
        },
        "differences": [
            {
                "topic": "Christological formulae",
                "eo": "One Person in two natures; two wills and energies in harmony.",
                "oo": "One united incarnate nature; acknowledges full humanity/divinity but wary of 'two natures' post-union."
            },
            {
                "topic": "Post‑Chalcedonian saints and councils",
                "eo": "Receives later councils and saints like St. Maximus, St. John Damascene.",
                "oo": "Venerates figures like St. Severus of Antioch; hesitates to receive later Byzantine councils."
            },
            {
                "topic": "Liturgical families",
                "eo": "Byzantine rite with local usages.",
                "oo": "Alexandrian, West Syriac, Armenian, Ge'ez, and Malankara rites; ethos very similar."
            }
        ],
        "dialogue": {
            "convergences": [
                "Official joint statements suggest disputes were often linguistic, not dogmatic.",
                "Mutual rejection of Eutychianism and Nestorianism.",
                "Strong agreement on deification, sacramental life, and Scripture–Tradition balance."
            ],
            "remaining_obstacles": [
                "Reception of Chalcedon and later councils.",
                "Status of post‑schism saints and anathemas.",
                "Official phrasing about wills/energies and natures that both families can receive.",
                "Practical integration of hierarchies and jurisdictions."
            ]
        },
        "today": {
            "communion": "Not in full communion yet.",
            "mutual_recognition": [
                "Baptisms commonly recognized.",
                "Mixed marriages sometimes blessed (with episcopal oversight).",
                "Ongoing theological commissions and local pastoral accommodations."
            ]
        },
        "timeline": [
            {"year": 325, "event": "Council of Nicaea I"},
            {"year": 381, "event": "Council of Constantinople I"},
            {"year": 431, "event": "Council of Ephesus"},
            {"year": 451, "event": "Council of Chalcedon (split in reception)"},
            {"year": 553, "event": "Second Council of Constantinople (EO reception)"},
            {"year": 680, "event": "Third Council of Constantinople affirms two wills/energies (EO)"},
            {"year": 787, "event": "Second Council of Nicaea (icons; EO)"},
            {"year": 1964, "event": "Renewed dialogue between EO and OO"},
            {"year": 1990, "event": "Notable joint statements clarifying Christology"}
        ],
        "glossary": [
            {"term": "Miaphysite", "definition": "Confession of one united incarnate nature of the Word (Cyrillian), not denying Christ’s humanity."},
            {"term": "Dyophysite", "definition": "Confession that Christ is one Person in two natures, without confusion or separation (Chalcedonian)."},
            {"term": "Chalcedon", "definition": "Council in AD 451; taught Christ is one Person in two natures; reception divided EO and OO."},
            {"term": "Theotokos", "definition": "Title of Mary as 'God-bearer', affirmed by both families."},
            {"term": "Theosis", "definition": "Deification; participation in God’s life by grace, central to both traditions."}
        ],
        "takeaways": [
            "Faith and life are remarkably close.",
            "The divide centers on expression about the one Christ, not different faiths in Him.",
            "Full communion requires shared statements, lifting anathemas, and agreement on later councils."
        ]
    }

@app.get("/api/overview")
def get_overview():
    return build_overview()


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
