CREATE TABLE JournalEntries (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  concept TEXT NOT NULL,
  entry TEXT NOT NULL,
  date INTEGER NOT NULL,
  moodId REFERENCES Moods(id)
);

CREATE TABLE Moods (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  label TEXT NOT NULL
);

INSERT INTO `Moods` VALUES (null, 'Happy');
INSERT INTO `Moods` VALUES (null, 'Sad');
INSERT INTO `Moods` VALUES (null, 'Angry');
INSERT INTO `Moods` VALUES (null, 'Ok');


INSERT INTO JournalEntries VALUES (null, '1234', '123', 1598458543321, 1);
INSERT INTO JournalEntries VALUES (null, 'abc', '123', 1598458548239, 2);
INSERT INTO JournalEntries VALUES (null, 'Delete', 'Now Deleting', 1598458559152, 1);
INSERT INTO JournalEntries VALUES (null, 'ANGRY', 'fgfgdfg', 1598557358781, 3);
INSERT INTO JournalEntries VALUES (null, '678', 'Now Deleting', 1598557373697, 4)

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

SELECT * from JournalEntries
