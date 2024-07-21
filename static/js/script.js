//////////////////////  SEARCH BAR ELONGATION ///////////////////////
document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.getElementById('searchButton');
    const searchBar = document.getElementById('searchBar');
    const searchInput = document.getElementById('searchInput');
    const closeIcon = document.getElementById('closeIcon');
  
    searchButton.addEventListener('click', function() {
      searchBar.classList.add('expanded');
      searchInput.focus();
    });
  
    closeIcon.addEventListener('click', function() {
      searchBar.classList.remove('expanded');
      searchInput.value = '';
    });
  
    // Optionally close the search bar when clicking outside
    document.addEventListener('click', function(event) {
      if (!searchBar.contains(event.target) && !searchButton.contains(event.target)) {
        searchBar.classList.remove('expanded');
        searchInput.value = '';
      }
    });
  });
  
