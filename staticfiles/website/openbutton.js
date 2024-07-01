document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll("[id^=popupButton]");
    
    buttons.forEach(button => {
        const id = button.id.replace("popupButton", "");
        const popup = document.getElementById(`popup${id}`);
        const editButton = document.getElementById(`editButton${id}`);
        const deleteButton = document.getElementById(`deleteButton${id}`);

        button.addEventListener("click", function(event) {
            // Toggle popup visibility
            popup.style.display = popup.style.display === "block" ? "none" : "block";
            button.style.display = button.style.display === "none" ? "inline-block":"none";
            // Position the popup
            const rect = button.getBoundingClientRect();
            popup.style.top = `${rect.bottom + window.scrollY}px`;
            popup.style.left = `${rect.left + window.scrollX}px`;
        });

        // Add click event listeners for the edit and delete buttons
        editButton.addEventListener("click", function() {
            popup.style.display = "none";
            button.style.display = "inline-block";
        });

        deleteButton.addEventListener("click", function() {
            popup.style.display = "none";
            button.style.display = "inline-block";
        });
    });

    document.addEventListener("click", function(event) {
        buttons.forEach(button => {
            const id = button.id.replace("popupButton", "");
            const popup = document.getElementById(`popup${id}`);
            if (!button.contains(event.target) && !popup.contains(event.target)) {
                popup.style.display = "none";
                button.style.display = "inline-block"
            }
        });
    });
});