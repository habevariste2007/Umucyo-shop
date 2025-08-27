let journalData = [];
let editIndex = -1;

// Load data from server
async function loadDataFromServer() {
    try {
        const res = await fetch("/get-data");
        const data = await res.json();
        journalData = data.journal || [];
        updateTable();
    } catch (err) {
        console.error("Failed to load data", err);
    }
}

// Save data to server
async function saveDataToServer() {
    try {
        const data = { journal: journalData };
        await fetch("/save-data", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });
    } catch (err) {
        console.error("Failed to save data", err);
    }
}

// Dummy updateTable if not defined
function updateTable() {
    console.log("updateTable called with", journalData);
}

// Example: call loadData when page loads
window.addEventListener("DOMContentLoaded", loadDataFromServer);
