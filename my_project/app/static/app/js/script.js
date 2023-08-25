document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('update-button').addEventListener('click', () => {
        fetch('/update-data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                alert('An error occurred while updating the data.');
            }
        });
    });
});