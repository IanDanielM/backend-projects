import csv
import os
from typing import Any, Dict, List


class CSVHelper:
    def __init__(self, filename: str, mode: str = 'r', headers: List[str] = None):
        self.filename = filename
        self.mode = mode
        self.headers = headers
        self.file = None
        self.reader = None
        self.writer = None

    def __enter__(self):
        file_exists = os.path.exists(self.filename)
        file_empty = file_exists and os.path.getsize(self.filename) == 0

        if 'a' in self.mode:
            self.file = open(self.filename, self.mode, newline='')
            if file_empty or not file_exists:
                self.writer = csv.DictWriter(self.file, fieldnames=self.headers)
                self.writer.writeheader()
            else:
                with open(self.filename, 'r', newline='') as f:
                    reader = csv.reader(f)
                    file_headers = next(reader, None)
                self.writer = csv.DictWriter(self.file, fieldnames=file_headers)
        else:
            if not file_exists and 'r' in self.mode:
                open(self.filename, 'w').close()

            if 'r' in self.mode and '+' not in self.mode:
                self.mode += '+'
                
            self.file = open(self.filename, self.mode, newline='')

            if 'r' in self.mode:
                self.reader = csv.DictReader(self.file)
                if not file_exists and self.headers:
                    self.reader.fieldnames = self.headers
            if 'w' in self.mode or '+' in self.mode:
                fieldnames = self.headers or (
                    self.reader.fieldnames if self.reader else None)
                self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
                if 'w' in self.mode or (not file_exists and '+' in self.mode):
                    self.writer.writeheader()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def read_all(self) -> List[Dict[str, Any]]:
        self.file.seek(0)
        return list(csv.DictReader(self.file))

    def read_row(self, row_number) -> Dict[str, Any]:
        for i, row in enumerate(self.reader):
            if i == row_number:
                return row
        raise IndexError("Out of Range")

    def write_row(self, row: Dict[str, Any]):
        self.writer.writerow(row)

    def write_rows(self, rows: List[Dict[str, Any]]):
        self.file.seek(0)
        self.file.truncate()
        self.writer.writeheader()
        self.writer.writerows(rows)

    def update_row(self, row_number: int, updated_row: Dict[str, Any]) -> List[Dict[str, Any]]:
        rows = self.read_all()
        if 1 <= row_number <= len(rows):
            rows[row_number - 1].update(updated_row)
            self.write_rows(rows)
        else:
            raise IndexError("Out of range")

    def delete_row(self, row_number: int) -> List[Dict[str, Any]]:
        rows = self.read_all()
        if 1 <= row_number <= len(rows):
            del rows[row_number - 1]
            self.write_rows(rows)
        else:
            raise IndexError("Out Of Range")
