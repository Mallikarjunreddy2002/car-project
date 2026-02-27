document.addEventListener('DOMContentLoaded', function() {
    const deleteLinks = document.querySelectorAll('.delete-link');

    deleteLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            const confirmDelete = confirm("Are you sure you want to delete this car?");
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });
});
