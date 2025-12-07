// ===== KI-TOOL-ANALYSEN - INTERACTIVE SCRIPT =====

// Update current date and week number
function updateDateInfo() {
    const now = new Date();
    const dateElement = document.getElementById('currentDate');
    const weekElement = document.getElementById('weekNumber');
    
    if (dateElement) {
        const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
        dateElement.textContent = now.toLocaleDateString('de-DE', options);
    }
    
    if (weekElement) {
        const weekNumber = getWeekNumber(now);
        weekElement.textContent = `KW ${weekNumber}`;
    }
}

// Calculate week number
function getWeekNumber(date) {
    const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
    const dayNum = d.getUTCDay() || 7;
    d.setUTCDate(d.getUTCDate() + 4 - dayNum);
    const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
    return Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
}

// Filter functionality
function initializeFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const toolCards = document.querySelectorAll('.tool-card');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.dataset.filter;
            
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            // Filter cards
            toolCards.forEach(card => {
                if (filter === 'all') {
                    card.classList.remove('hidden');
                } else {
                    if (card.dataset.category === filter) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                }
            });
            
            // Animate filtered cards
            setTimeout(() => {
                const visibleCards = document.querySelectorAll('.tool-card:not(.hidden)');
                visibleCards.forEach((card, index) => {
                    card.style.animation = 'none';
                    setTimeout(() => {
                        card.style.animation = `fadeInUp 0.5s ease ${index * 0.1}s forwards`;
                    }, 10);
                });
            }, 50);
        });
    });
}

// Show tool details (placeholder for future modal/page)
function showToolDetails(toolId) {
    console.log(`Showing details for: ${toolId}`);
    
    // Tool details mapping
    const toolDetails = {
        'proofly': {
            name: 'Proofly',
            url: 'https://chromewebstore.google.com/detail/proofly',
            description: 'On-Device AI Proofreader'
        },
        'bloom': {
            name: 'Bloom',
            url: 'https://www.trybloom.ai/',
            description: 'AI Brand Asset Generator'
        },
        'nume': {
            name: 'Nume',
            url: 'https://www.nume.ai/',
            description: 'AI CFO für Startups'
        },
        'exa': {
            name: 'Exa',
            url: 'https://exa.ai/',
            description: 'AI Search Engine für Agents'
        },
        'notis': {
            name: 'Notis',
            url: 'https://notis.ai/',
            description: 'Autonomous AI Agent'
        }
    };
    
    const tool = toolDetails[toolId];
    if (tool) {
        // For now, just show an alert. In future, this could open a modal or navigate to a detail page
        const message = `${tool.name}\n\n${tool.description}\n\nWebsite: ${tool.url}\n\nDetaillierte Analyse wird in Kürze verfügbar sein.`;
        alert(message);
        
        // Optional: Open tool website in new tab
        // window.open(tool.url, '_blank');
    }
}

// Smooth scroll to top
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Add scroll-to-top button
function addScrollToTopButton() {
    const button = document.createElement('button');
    button.innerHTML = '↑';
    button.className = 'scroll-to-top';
    button.style.cssText = `
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 50px;
        height: 50px;
        background: var(--cyber-primary);
        color: var(--text-primary);
        border: 2px solid var(--cyber-primary);
        border-radius: 50%;
        font-size: 1.5rem;
        font-weight: 700;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 1000;
        box-shadow: 0 4px 12px rgba(0, 255, 157, 0.3);
    `;
    
    button.addEventListener('click', scrollToTop);
    document.body.appendChild(button);
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            button.style.opacity = '1';
            button.style.visibility = 'visible';
        } else {
            button.style.opacity = '0';
            button.style.visibility = 'hidden';
        }
    });
    
    // Hover effect
    button.addEventListener('mouseenter', () => {
        button.style.transform = 'translateY(-4px) scale(1.1)';
        button.style.boxShadow = '0 6px 20px rgba(0, 255, 157, 0.5)';
    });
    
    button.addEventListener('mouseleave', () => {
        button.style.transform = 'translateY(0) scale(1)';
        button.style.boxShadow = '0 4px 12px rgba(0, 255, 157, 0.3)';
    });
}

// Animate cards on scroll
function animateOnScroll() {
    const cards = document.querySelectorAll('.tool-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1
    });
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

// Add CSS animation keyframes dynamically
function addAnimations() {
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);
}

// Initialize all features
function init() {
    updateDateInfo();
    initializeFilters();
    addScrollToTopButton();
    animateOnScroll();
    addAnimations();
    
    console.log('KI-Tool-Analysen initialized successfully! 🚀');
}

// Run initialization when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

// Make showToolDetails globally available
window.showToolDetails = showToolDetails;
