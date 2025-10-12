// ===== PARTICLE.JS CONFIGURATION =====
particlesJS('particles-js', {
    particles: {
        number: {
            value: 80,
            density: {
                enable: true,
                value_area: 800
            }
        },
        color: {
            value: ['#ff0050', '#ff4081', '#00ffff', '#ff00ff']
        },
        shape: {
            type: 'circle',
            stroke: {
                width: 0,
                color: '#000000'
            }
        },
        opacity: {
            value: 0.5,
            random: true,
            anim: {
                enable: true,
                speed: 1,
                opacity_min: 0.1,
                sync: false
            }
        },
        size: {
            value: 3,
            random: true,
            anim: {
                enable: true,
                speed: 2,
                size_min: 0.1,
                sync: false
            }
        },
        line_linked: {
            enable: true,
            distance: 150,
            color: '#ff0050',
            opacity: 0.4,
            width: 1
        },
        move: {
            enable: true,
            speed: 2,
            direction: 'none',
            random: false,
            straight: false,
            out_mode: 'out',
            bounce: false,
            attract: {
                enable: false,
                rotateX: 600,
                rotateY: 1200
            }
        }
    },
    interactivity: {
        detect_on: 'canvas',
        events: {
            onhover: {
                enable: false,
                mode: 'repulse'
            },
            onclick: {
                enable: false,
                mode: 'push'
            },
            resize: true
        },
        modes: {
            grab: {
                distance: 400,
                line_linked: {
                    opacity: 1
                }
            },
            bubble: {
                distance: 400,
                size: 40,
                duration: 2,
                opacity: 8,
                speed: 3
            },
            repulse: {
                distance: 100,
                duration: 0.4
            },
            push: {
                particles_nb: 4
            },
            remove: {
                particles_nb: 2
            }
        }
    },
    retina_detect: true
});

// ===== DOWNLOAD FUNCTIONALITY =====
document.addEventListener('DOMContentLoaded', function() {
    const downloadButtons = document.querySelectorAll('.download-btn');
    
    downloadButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.glass-card');
            const progressContainer = card.querySelector('.progress-container');
            const progressBar = card.querySelector('.progress-bar');
            const downloadUrl = this.dataset.url;
            
            // Show progress bar
            progressContainer.style.display = 'block';
            
            // Disable button during download
            this.disabled = true;
            this.style.opacity = '0.7';
            
            // Simulate download progress
            let progress = 0;
            const interval = setInterval(() => {
                progress += Math.floor(Math.random() * 15) + 5;
                
                if (progress >= 100) {
                    progress = 100;
                    clearInterval(interval);
                    
                    // Start actual download
                    window.location.href = downloadUrl;
                    
                    // Reset after download
                    setTimeout(() => {
                        progressBar.style.width = '0%';
                        progressContainer.style.display = 'none';
                        this.disabled = false;
                        this.style.opacity = '1';
                    }, 1500);
                }
                
                progressBar.style.width = progress + '%';
            }, 200);
        });
    });
    
    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// ===== CONSOLE WELCOME MESSAGE =====
console.log('%c🚀 Welcome to Tabbu Arain\'s APK Download Center!', 'color: #ff0050; font-size: 20px; font-weight: bold;');
console.log('%c💫 Powered by Flask & Particle.js', 'color: #00ffff; font-size: 14px;');
