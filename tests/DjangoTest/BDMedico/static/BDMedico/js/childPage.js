// Get menu links
const links = document.querySelectorAll('.menu a');
// childPage.js
console.log("El archivo childPage.js se ha cargado exitosamente.");

// Add click event to each link 
links.forEach(link => {

  link.addEventListener('click', e => {

    e.preventDefault();
    
    // Get page to load
    const page = link.getAttribute('href'); 

    // Load page content with Fetch API
    fetch(page)
      .then(response => response.text())
      .then(html => {
        
        // Insert HTML into content div
        document.querySelector('#content').innerHTML = html;
      });

  });

});