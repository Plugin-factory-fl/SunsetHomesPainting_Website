// Sunset Homes Painting - Main JavaScript

// Gallery Modal Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize gallery modals
    initGalleryModals();

    // Initialize form validation
    initFormValidation();

    // Homepage hero image slideshow
    initHomeHeroSlideshow();
});

// Homepage hero slideshow (20/21 before-after first, then more project photos)
function initHomeHeroSlideshow() {
    const root = document.querySelector('.home-hero-slideshow');
    if (!root) return;

    const track = root.querySelector('.home-hero-slideshow-track');
    const slides = root.querySelectorAll('.home-hero-slide');
    const prevBtn = root.querySelector('[data-slide-dir="prev"]');
    const nextBtn = root.querySelector('[data-slide-dir="next"]');
    if (!track || slides.length === 0) return;

    let index = 0;
    let timer = null;
    const intervalMs = parseInt(root.getAttribute('data-autoplay-ms'), 10) || 3000;
    const hoverZone = root.closest('.home-image-section') || root;

    function isHoverPaused() {
        return hoverZone.matches(':hover');
    }

    function goTo(nextIndex) {
        index = ((nextIndex % slides.length) + slides.length) % slides.length;
        track.style.transform = 'translateX(-' + (index * 100) + '%)';
        slides.forEach(function(slide, i) {
            slide.setAttribute('aria-hidden', i === index ? 'false' : 'true');
        });
    }

    function next() {
        goTo(index + 1);
    }

    function prev() {
        goTo(index - 1);
    }

    function startAutoplay() {
        stopAutoplay();
        timer = setInterval(next, intervalMs);
    }

    function stopAutoplay() {
        if (timer) {
            clearInterval(timer);
            timer = null;
        }
    }

    function restartAutoplay() {
        stopAutoplay();
        if (!isHoverPaused()) {
            startAutoplay();
        }
    }

    function pauseForHover() {
        stopAutoplay();
    }

    function resumeAfterHover() {
        if (!isHoverPaused()) {
            startAutoplay();
        }
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            prev();
            restartAutoplay();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            next();
            restartAutoplay();
        });
    }

    hoverZone.addEventListener('mouseenter', pauseForHover);
    hoverZone.addEventListener('mouseleave', resumeAfterHover);
    root.addEventListener('focusin', pauseForHover);
    root.addEventListener('focusout', function(e) {
        if (!root.contains(e.relatedTarget) && !isHoverPaused()) {
            startAutoplay();
        }
    });

    goTo(0);
    startAutoplay();
}

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
