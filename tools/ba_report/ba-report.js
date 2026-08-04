/* BA Report Interactivity — Mermaid init, navigation, smooth scroll */

(function () {
  "use strict";

  // Initialize Mermaid on DOM ready
  document.addEventListener("DOMContentLoaded", function () {
    // Initialize Mermaid if available
    if (typeof mermaid !== "undefined") {
      mermaid.initialize({
        startOnLoad: true,
        theme: "default",
        securityLevel: "loose",
        flowchart: {
          useMaxWidth: true,
          htmlLabels: true,
          curve: "basis",
        },
        sequence: {
          useMaxWidth: true,
        },
        gantt: {
          useMaxWidth: true,
        },
      });
      console.log("[ba-report] Mermaid initialized");
    } else {
      console.warn("[ba-report] Mermaid not loaded — diagrams will not render");
    }

    // Smooth scroll for navigation links
    initSmoothScroll();

    // Highlight active nav item on scroll
    initScrollSpy();
  });

  /**
   * Smooth scroll for navigation links
   */
  function initSmoothScroll() {
    const navLinks = document.querySelectorAll(".ss-ba-nav a[href^='#']");

    navLinks.forEach(function (link) {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        const targetId = link.getAttribute("href").substring(1);
        const target = document.getElementById(targetId);

        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
            block: "start",
          });

          // Update URL hash without scrolling
          if (history.pushState) {
            history.pushState(null, null, "#" + targetId);
          } else {
            location.hash = "#" + targetId;
          }
        }
      });
    });
  }

  /**
   * Scroll spy — highlight active nav item based on scroll position
   */
  function initScrollSpy() {
    const navLinks = document.querySelectorAll(".ss-ba-nav a[href^='#']");
    const sections = [];

    // Collect all target sections
    navLinks.forEach(function (link) {
      const targetId = link.getAttribute("href").substring(1);
      const section = document.getElementById(targetId);
      if (section) {
        sections.push({
          id: targetId,
          element: section,
          link: link,
        });
      }
    });

    if (sections.length === 0) return;

    // Update active state on scroll
    function updateActive() {
      const scrollPos = window.scrollY + 100; // offset for sticky nav

      let activeSection = sections[0];

      for (let i = 0; i < sections.length; i++) {
        const section = sections[i];
        const top = section.element.offsetTop;

        if (scrollPos >= top) {
          activeSection = section;
        }
      }

      // Update nav links
      navLinks.forEach(function (link) {
        link.style.color = "";
        link.style.fontWeight = "";
      });

      if (activeSection) {
        activeSection.link.style.color = "var(--ss-accent, #10a37f)";
        activeSection.link.style.fontWeight = "600";
      }
    }

    // Throttle scroll handler
    let scrollTimeout;
    window.addEventListener("scroll", function () {
      if (scrollTimeout) {
        clearTimeout(scrollTimeout);
      }
      scrollTimeout = setTimeout(updateActive, 100);
    });

    // Initial update
    updateActive();
  }
})();
