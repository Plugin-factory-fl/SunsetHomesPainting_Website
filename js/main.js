// Sunset Homes Painting - Main JavaScript

// Gallery Modal Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize gallery modals
    initGalleryModals();
    
    // Initialize form validation
    initFormValidation();
    
    // Set active nav link based on current page
    setActiveNavLink();
});

// Gallery Modal Functions
function initGalleryModals() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    galleryItems.forEach(item => {
        // Click handler
        item.addEventListener('click', function() {
            openGalleryModal(this);
        });
        
        // Keyboard handler for accessibility (Enter and Space keys)
        item.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                openGalleryModal(this);
            }
        });
    });
}

function openGalleryModal(item) {
    const img = item.querySelector('img');
    const caption = item.querySelector('.gallery-caption');
    
    if (img && caption) {
        openImageModal(img.src, img.alt, caption.textContent);
    }
}

function openImageModal(imageSrc, imageAlt, caption) {
    // Create modal HTML
    const modalHTML = `
        <div class="modal fade" id="imageModal" tabindex="-1" aria-labelledby="imageModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="imageModalLabel">${caption}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <img src="${imageSrc}" alt="${imageAlt}" class="img-fluid">
                    </div>
                </div>
            </div>
        </div>
    `;
    
    // Remove existing modal if any
    const existingModal = document.getElementById('imageModal');
    if (existingModal) {
        existingModal.remove();
    }
    
    // Add modal to body
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    
    // Initialize and show Bootstrap modal
    const modalElement = document.getElementById('imageModal');
    const modal = new bootstrap.Modal(modalElement);
    modal.show();
    
    // Clean up modal when hidden
    modalElement.addEventListener('hidden.bs.modal', function() {
        modalElement.remove();
    });
}

// Form Validation
function initFormValidation() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (validateForm()) {
                // Form is valid - in production, this would submit to server
                showFormSuccess();
                // Uncomment the line below to actually submit (when backend is ready)
                // contactForm.submit();
            }
        });
        
        // Real-time validation on blur
        const formFields = contactForm.querySelectorAll('input, textarea');
        formFields.forEach(field => {
            field.addEventListener('blur', function() {
                validateField(this);
            });
            
            field.addEventListener('input', function() {
                // Clear error when user starts typing
                if (this.classList.contains('is-invalid')) {
                    clearFieldError(this);
                }
            });
        });
    }
}

function validateForm() {
    const form = document.getElementById('contactForm');
    let isValid = true;
    
    // Validate name
    const nameField = form.querySelector('#name');
    if (!validateField(nameField)) {
        isValid = false;
    }
    
    // Validate email
    const emailField = form.querySelector('#email');
    if (!validateField(emailField)) {
        isValid = false;
    }
    
    // Validate phone
    const phoneField = form.querySelector('#phone');
    if (!validateField(phoneField)) {
        isValid = false;
    }
    
    // Validate message
    const messageField = form.querySelector('#message');
    if (!validateField(messageField)) {
        isValid = false;
    }
    
    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let errorMessage = '';
    
    // Check if required field is empty
    if (field.hasAttribute('required') && value === '') {
        isValid = false;
        errorMessage = 'This field is required.';
    }
    
    // Email validation
    if (field.type === 'email' && value !== '') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address.';
        }
    }
    
    // Phone validation (basic - allows various formats)
    if (field.type === 'tel' && value !== '') {
        const phoneRegex = /^[\d\s\-\(\)\+]+$/;
        if (!phoneRegex.test(value) || value.replace(/\D/g, '').length < 10) {
            isValid = false;
            errorMessage = 'Please enter a valid phone number.';
        }
    }
    
    // Message length validation
    if (field.tagName === 'TEXTAREA' && value !== '') {
        if (value.length < 10) {
            isValid = false;
            errorMessage = 'Please enter a message with at least 10 characters.';
        }
    }
    
    // Display error or clear it
    if (!isValid) {
        showFieldError(field, errorMessage);
    } else {
        clearFieldError(field);
    }
    
    return isValid;
}

function showFieldError(field, message) {
    field.classList.add('is-invalid');
    field.classList.remove('is-valid');
    
    // Remove existing error message
    const existingError = field.parentElement.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
    
    // Add error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    field.parentElement.appendChild(errorDiv);
}

function clearFieldError(field) {
    field.classList.remove('is-invalid');
    field.classList.add('is-valid');
    
    const errorDiv = field.parentElement.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

function showFormSuccess() {
    const form = document.getElementById('contactForm');
    const successMessage = document.createElement('div');
    successMessage.className = 'alert alert-success mt-3';
    successMessage.setAttribute('role', 'alert');
    successMessage.innerHTML = '<strong>Thank you!</strong> Your message has been sent. We will get back to you soon.';
    
    // Remove existing success message if any
    const existingSuccess = form.querySelector('.alert-success');
    if (existingSuccess) {
        existingSuccess.remove();
    }
    
    form.appendChild(successMessage);
    form.reset();
    
    // Remove validation classes
    form.querySelectorAll('.is-valid, .is-invalid').forEach(field => {
        field.classList.remove('is-valid', 'is-invalid');
    });
    
    // Scroll to success message
    successMessage.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    
    // Remove success message after 5 seconds
    setTimeout(() => {
        successMessage.remove();
    }, 5000);
}

// Set active navigation link based on current page
function setActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        const linkHref = link.getAttribute('href');
        if (linkHref === currentPage || 
            (currentPage === '' && linkHref === 'index.html') ||
            (currentPage === 'index.html' && linkHref === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Smooth scroll for anchor links (if needed)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.length > 1) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});
