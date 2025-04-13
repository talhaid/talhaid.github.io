// Mobile menu toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Close mobile menu when clicking on a link
    const mobileMenuLinks = mobileMenu?.querySelectorAll('a');
    if (mobileMenuLinks) {
        mobileMenuLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.add('hidden');
            });
        });
    }

    // Simple form validation for contact form
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form elements
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const messageInput = document.getElementById('message');
            
            // Simple validation
            let isValid = true;
            
            if (!nameInput.value.trim()) {
                nameInput.classList.add('border-red-500');
                isValid = false;
            } else {
                nameInput.classList.remove('border-red-500');
            }
            
            if (!emailInput.value.trim() || !isValidEmail(emailInput.value)) {
                emailInput.classList.add('border-red-500');
                isValid = false;
            } else {
                emailInput.classList.remove('border-red-500');
            }
            
            if (!messageInput.value.trim()) {
                messageInput.classList.add('border-red-500');
                isValid = false;
            } else {
                messageInput.classList.remove('border-red-500');
            }
            
            // If valid, we would normally submit the form
            // For now just show a success message
            if (isValid) {
                alert('Form submitted successfully! This is a placeholder for actual form submission.');
                contactForm.reset();
            }
        });
    }

    // Helper function to validate email
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Add smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Project filtering functionality (for future enhancement)
// This is a placeholder for future filtering capabilities
function setupProjectFilters() {
    // This functionality can be expanded in the future
    console.log('Project filtering ready to be implemented');
}

// Add a simple dark/light mode toggle (can be expanded later)
function setupThemeToggle() {
    // Can be implemented later when needed
    console.log('Theme toggle ready to be implemented');
}

// Add animation on scroll (can be implemented with libraries like AOS)
function initializeAnimations() {
    // Can be implemented with a library or custom code later
    console.log('Scroll animations ready to be implemented');
}
