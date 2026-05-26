# Live USD-to-NGN FX Rate Monitor

A full-stack, automated financial tracking pipeline that extracts live USD to Nigerian Naira (NGN) exchange metrics, caches the payload via a secure backend gateway, and pushes dynamic client updates using an asynchronous web user interface.

## 🏗️ System Blueprint & Operational Lifecycle

1. **Extraction Layer (`scraper.py`)**: A native Python script polls the ExchangeRate-API system, targets the specific `NGN` conversion asset matrix, isolates the raw float data, and dispatches an authenticated multi-part payload.
2. **API Caching Gateway (`process_data.php`)**: A lightweight REST endpoint parses incoming pipeline parameters via `POST` methods, passes string tokens through sanitization filters, and serializes the state down to a persistent local flat-file storage structure (`rates.json`).
3. **Reactive Presentation Layer (`app.js`)**: The frontend layout relies on a client-side execution cycle via native JavaScript `Fetch` mechanisms (`GET`), restructuring target elements within the DOM structure dynamically on load or explicit manual update events.

## 🚀 Architectural Advantages

* **No-Dependency Core Build**: Built using entirely native libraries—Python `urllib`, vanilla ECMAScript 6+, and structural core PHP routines—ensuring zero third-party vulnerability vectors.
* **Aggressive Data Protection**: Leverages internal backend filters (`FILTER_SANITIZE_SPECIAL_CHARS`, `FILTER_VALIDATE_FLOAT`) on data ingestion cycles to mitigate malicious script injections.
* **Server-Side Cache Decoupling**: Saves incoming structures into a server-side JSON file cache, decoupling expensive database execution tasks from standard front-end client reads.
* **Optimized API Overhead**: Restricts payload transmissions strictly to targeted variables (`currency`, `rate`, `updated_at`), lowering bandwidth overhead across network routers.

## 🛠️ Technology Stack Breakdown

* **Automation Engine**: Python 3.x (`json`, `urllib.request`, `urllib.parse`).
* **Gateway Layer**: Core PHP 8.x Web Controller Engine.
* **Data Layer**: Flat-file JSON Schema Structs (`rates.json`).
* **Frontend Matrix**: Structural HTML5, Native CSS Grid Layouts, Vanilla JavaScript (Async/Await Fetch Architecture).

## 🗂️ Project Structure

```text
├── assets/
│   ├── css/
│   │   └── style.css           # Component presentation styles & visual cards
│   └── js/
│   │   └── app.js              # Client-side state broker & DOM compiler
├── backend/
│   ├── process_data.php        # Transaction split router (POST ingest / GET egress)
│   └── rates.json              # Local flat-file persistence layer
├── pipeline/
│   └── scraper.py              # Single-currency automation mining script
└── index.html                  # Core presentation layer user interface dashboard
```

## 🔌 Operational API Endpoints

### 1. Ingestion Protocol
* **Method Type**: `POST`
* **Target Interface**: `/backend/process_data.php`
* **Form Structure Payload**:
  * `currency` (string): Set to `"NGN"`.
  * `rate` (float): Current currency calculation metrics.
  * `updated_at` (string): String representation of the source database timestamp.

### 2. Client Matrix Egress
* **Method Type**: `GET`
* **Target Interface**: `/backend/process_data.php`
* **JSON Format Structure Output**:
  ```json
  {
    "currency": "NGN",
    "rate": 1602.50,
    "updated_at": "Tue, 26 May 2026 14:30:00 UTC",
    "last_checked": "2026-05-26 15:35:12"
  }
  ```

## ⚙️ Execution & Verification Guide

### Step 1: Deploy Project Directories
Clone this project workspace down to your target machine root or local PHP service layer environment:
```bash
git clone https://github.com
cd usd-ngn-rate-monitor
```

### Step 2: Initialize Web Services
Spin up your chosen server tool stack (XAMPP, Apache, or built-in PHP modules) from your project root folder directory:
```bash
php -S localhost:80
```

### Step 3: Execute Core Mining Script
Fire off your data generation worker via a separate runtime terminal terminal shell window to ingest active records:
```bash
python pipeline/scraper.py
```

### Step 4: Verify Dashboard Sync
Load up `http://localhost:80/index.html` within your preferred internet browser engine. Hit **"Refresh Dashboard"** to observe your pipeline updating information directly to the dashboard interface!
