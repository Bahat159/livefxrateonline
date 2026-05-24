<?php
// Allow the frontend to access this file safely
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

$file_path = "rates.json";

// 1. Handle incoming POST request from Python script
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $currency = filter_input(INPUT_POST, 'currency', FILTER_SANITIZE_SPECIAL_CHARS);
    $rate = filter_input(INPUT_POST, 'rate', FILTER_VALIDATE_FLOAT);
    $updated_at = filter_input(INPUT_POST, 'updated_at', FILTER_SANITIZE_SPECIAL_CHARS);

    if ($currency && $rate && $updated_at) {
        $data_to_save = [
            "currency" => $currency,
            "rate" => round($rate, 2),
            "updated_at" => $updated_at,
            "last_checked" => date("Y-m-d H:i:s")
        ];

        // Save data cleanly to a JSON file
        file_put_contents($file_path, json_encode($data_to_save, JSON_PRETTY_PRINT));
        echo json_encode(["status" => "success", "message" => "Rates updated successfully."]);
        exit;
    } else {
        http_response_code(400);
        echo json_encode(["status" => "error", "message" => "Invalid data received."]);
        exit;
    }
}

// 2. Handle incoming GET request from Frontend JavaScript
if ($_SERVER["REQUEST_METHOD"] === "GET") {
    if (file_exists($file_path)) {
        echo file_get_contents($file_path);
    } else {
        // Default fallback data if Python hasn't run yet
        echo json_encode([
            "currency" => "NGN",
            "rate" => 0.00,
            "updated_at" => "No data yet. Run scraper.py",
            "last_checked" => "Never"
        ]);
    }
    exit;
}
?>
