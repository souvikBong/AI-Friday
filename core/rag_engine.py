import sqlite3

class RAGEngine:
    def __init__(self, db_path="db/knowledge.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """)
        self.conn.commit()

        # insert demo knowledge
        cursor.execute("INSERT OR IGNORE INTO knowledge VALUES (?,?)",
                       ("clinical_trial_rules", "Trial allows adults with diabetes or hypertension. Steroids are excluded."))
        cursor.execute("INSERT OR IGNORE INTO knowledge VALUES (?,?)",
                       ("maintenance_guidelines", "Service every 1000 hours or 150 days as per manufacturer."))
        self.conn.commit()

    def lookup(self, key):
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM knowledge WHERE key=?", (key,))
        row = cursor.fetchone()
        return row[0] if row else "No KB data found"
