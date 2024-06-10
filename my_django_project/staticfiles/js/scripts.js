document.addEventListener('DOMContentLoaded', function() {
    // Form validation for registration
    const registerForm = document.querySelector('#registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            const password = document.querySelector('#password').value;
            const confirmPassword = document.querySelector('#confirmPassword').value;
            if (password !== confirmPassword) {
                event.preventDefault();
                alert('Passwords do not match!');
            }
        });
    }

    // Search suggestions
    const searchInput = document.querySelector('#generic-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = searchInput.value;
            if (query.length >= 3) {
                fetch(`/search_suggestions?q=${query}`)
                    .then(response => response.json())
                    .then(data => {
                        const suggestions = document.querySelector('#search-suggestions');
                        suggestions.innerHTML = '';
                        data.forEach(item => {
                            const suggestionItem = document.createElement('div');
                            suggestionItem.className = 'list-group-item';
                            suggestionItem.textContent = item.title;
                            suggestionItem.addEventListener('click', () => {
                                searchInput.value = item.title;
                                suggestions.innerHTML = '';
                            });
                            suggestions.appendChild(suggestionItem);
                        });
                        suggestions.style.display = 'block';
                    });
            } else {
                document.querySelector('#search-suggestions').style.display = 'none';
            }
        });
    }

    // Add to Watchlist functionality
    const addToWatchlistButtons = document.querySelectorAll('.add-to-watchlist');
    addToWatchlistButtons.forEach(button => {
        button.addEventListener('click', function() {
            const movieId = button.getAttribute('data-movie-id');
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            fetch(`/watchlist/add/${movieId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => {
                if (response.status === 401) {
                    window.location.href = "/login"; // Adjust if necessary
                    return;
                }
                return response.json();
            })
            .then(data => {
                if (data && data.success) {
                    button.classList.remove('btn-warning');
                    button.classList.add('btn-success');
                    button.textContent = 'Added';
                }
            });
        });
    });
});
