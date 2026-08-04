/* BA Report Interactivity — Mermaid init, navigation, scroll-spy */

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    if (typeof mermaid !== "undefined") {
      mermaid.initialize({
        startOnLoad: true,
        theme: "default",
        securityLevel: "loose",
        flowchart: { useMaxWidth: true, htmlLabels: true, curve: "basis" },
        sequence: { useMaxWidth: true },
        gantt: { useMaxWidth: true },
      });
    }

    initSmoothScroll();
    initScrollSpy();
  });

  function initSmoothScroll() {
    var navLinks = document.querySelectorAll(".ss-nav a[href^='#']");
    navLinks.forEach(function (link) {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        var targetId = link.getAttribute("href").substring(1);
        var target = document.getElementById(targetId);
        if (target) {
          target.scrollIntoView({ behavior: "smooth", block: "start" });
          if (history.pushState) {
            history.pushState(null, null, "#" + targetId);
          } else {
            location.hash = "#" + targetId;
          }
        }
      });
    });
  }

  function initScrollSpy() {
    var navLinks = document.querySelectorAll(".ss-nav a[href^='#']");
    var sections = [];

    navLinks.forEach(function (link) {
      var targetId = link.getAttribute("href").substring(1);
      var section = document.getElementById(targetId);
      if (section) {
        sections.push({ id: targetId, element: section, link: link });
      }
    });

    if (sections.length === 0) return;

    function updateActive() {
      var scrollPos = window.scrollY + 80;
      var activeSection = sections[0];

      for (var i = 0; i < sections.length; i++) {
        if (scrollPos >= sections[i].element.offsetTop) {
          activeSection = sections[i];
        }
      }

      navLinks.forEach(function (link) {
        link.classList.remove("is-active");
      });

      if (activeSection) {
        activeSection.link.classList.add("is-active");
      }
    }

    var scrollTimeout;
    window.addEventListener("scroll", function () {
      if (scrollTimeout) clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(updateActive, 100);
    });

    updateActive();
  }
})();
