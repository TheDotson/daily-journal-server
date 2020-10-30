import sqlite3
import json

from models import Entry, Mood

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          e.id,
          e.concept,
          e.entry,
          e.date,
          e.moodId,
          m.label
        FROM JournalEntries e
        JOIN moods m
            ON e.moodId = m.id
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
          entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row['moodId'])

          mood = Mood(row['moodId'], row['label'])

          entry.mood = mood.__dict__

          entries.append(entry.__dict__)

    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          e.id,
          e.concept,
          e.entry,
          e.date,
          e.moodId,
          m.label
        FROM JournalEntries e
        JOIN moods m
            ON e.moodId = m.id
        WHERE e.id = ?
        """, ( id, ))

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row['moodId'])

            mood = Mood(row['moodId'], row['label'])

            entry.mood = mood.__dict__

            entries.append(entry.__dict__)

        return json.dumps(entries)

def delete_entry(id):
    with sqlite3.connect('./dailyjournal.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM JournalEntries
        WHERE id = ?
        """, (id, ))


def get_entries_by_search(term):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(f"""
        select
            c.id,
            c.concept,
            c.entry,
            c.date,
            c.moodId
        FROM journalentries c
        WHERE c.entry LIKE '%{term}%'
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row['moodId'])
            
            entries.append(entry.__dict__)

    return json.dumps(entries)

def create_journal_entry(new_entry):
    with sqlite3.connect('./dailyjournal.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO JournalEntries
            (concept, entry, date, moodId)
        VALUES
            (?, ?, ?, ?)
        """, (new_entry['concept'], new_entry['entry'], new_entry['date'], new_entry['moodId']))

        id = db_cursor.lastrowid
        new_entry['id'] = id

    return json.dumps(new_entry)

def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE JournalEntries
            SET
                concept = ?,
                entry = ?,
                date = ?,
                moodId = ?
        WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'], new_entry['date'], new_entry['moodId'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
