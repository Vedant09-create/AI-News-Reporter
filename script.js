document.addEventListener('DOMContentLoaded', function () {
    let typingElements = document.querySelectorAll('.typing');

    // Typing effect function
    function typingEffect(element, speed, callback) {
        let text = element.getAttribute('data-text');
        let i = 0;
        element.innerHTML = '';

        function type() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            } else if (callback) {
                callback(); // Call the next effect when this one finishes
            }
        }

        type();
    }

    // Hide the second line initially
    const secondLine = typingElements[1];
    if (secondLine) {
        secondLine.style.visibility = 'hidden'; // Hide the second line
    }

    // Apply typing effect sequentially
    if (typingElements.length > 0) {
        typingEffect(typingElements[0], 100, function () {
            if (secondLine) {
                secondLine.style.visibility = 'visible'; // Show the second line
                typingEffect(secondLine, 100); // Start the second line typing effect
            }
        });
    }

    // Function to scroll to the next section after a certain time
    function autoScroll() {
        const sections = document.querySelectorAll('section');
        let currentSectionIndex = 0;

        function scrollToNextSection() {
            if (currentSectionIndex < sections.length - 1) {
                currentSectionIndex++;
                sections[currentSectionIndex].scrollIntoView({ behavior: 'smooth' });
            }
        }

        // Show and scroll through each section every 20 seconds
        sections.forEach((section, index) => {
            setTimeout(() => {
                section.style.display = 'block'; // Make the section visible
                if (index > 0) {
                    section.scrollIntoView({ behavior: 'smooth' });
                }
            }, index * 15000); // 20 seconds for each section
        });
    }

    // Start the auto scroll effect
    autoScroll();

    // Function to display the full story in Section 2


});
