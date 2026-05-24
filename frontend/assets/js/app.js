async function loadRates() {
    const rateText = document.getElementById('rate-text');
    const apiTime = document.getElementById('api-time');
    const syncTime = document.getElementById('sync-time');

    try {
        // Fetch the processed data from your PHP backend
        const response = await fetch('../backend/process_data.php');
        const data = await response.json();

        console.error(data);

        // Update HTML items dynamically
        rateText.textContent = `${data.rate.toLocaleString()} ₦`;
        apiTime.textContent = data.updated_at;
        syncTime.textContent = data.last_checked;
    } catch (error) {
        console.error("Error fetching data:", error);
        rateText.textContent = "Error ❌";
    }
}

// Load the rates automatically when the page opens
window.onload = loadRates;
