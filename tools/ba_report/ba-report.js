/* BA Report Interactivity — Mermaid init, navigation, scroll-spy */

(function () {
  "use strict";

  var navLinks, tocLinks, allEntries;

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

    navLinks = document.querySelectorAll(".ss-nav a[href^='#']");
    tocLinks = document.querySelectorAll(".ss-toc a[href^='#']");
    allEntries = [];

    buildEntries();
    initSmoothScroll();
    initScrollSpy();
  });

  function getHeaderOffset() {
    var header = document.querySelector(".ss-header");
    if (header) return header.offsetHeight + 16;
    return 80;
  }

  function scrollToTarget(target) {
    var y = target.getBoundingClientRect().top + window.pageYOffset - getHeaderOffset();
    window.scrollTo({ top: y, behavior: "smooth" });
  }

  function buildEntries() {
    navLinks.forEach(function (link) {
      var targetId = link.getAttribute("href").substring(1);
      var el = document.getElementById(targetId);
      if (!el) return;
      var existing = allEntries.find(function (e) { return e.id === targetId; });
      if (existing) { existing.navLink = link; }
      else { allEntries.push({ id: targetId, element: el, navLink: link, tocLink: null }); }
    });

    tocLinks.forEach(function (link) {
      var targetId = link.getAttribute("href").substring(1);
      var el = document.getElementById(targetId);
      if (!el) return;
      var existing = allEntries.find(function (e) { return e.id === targetId; });
      if (existing) { existing.tocLink = link; }
      else { allEntries.push({ id: targetId, element: el, navLink: null, tocLink: link }); }
    });
  }

  function setActive(id) {
    navLinks.forEach(function (l) { l.classList.remove("is-active"); });
    tocLinks.forEach(function (l) { l.classList.remove("is-active"); });

    var match = allEntries.find(function (s) { return s.id === id; });
    if (match) {
      if (match.navLink) match.navLink.classList.add("is-active");
      if (match.tocLink) match.tocLink.classList.add("is-active");
    }
  }

  function initSmoothScroll() {
    var allLinks = document.querySelectorAll(
      ".ss-nav a[href^='#'], .ss-sidebar a[href^='#'], .ss-toc a[href^='#'], .ss-ba-related[href^='#'], .ss-ba-artifact a[href^='#'], .ss-section-content a[href^='#']"
    );
    allLinks.forEach(function (link) {
      link.addEventListener("click", function (e) {
        var href = link.getAttribute("href");
        if (!href || href.charAt(0) !== "#") return;
        var targetId = href.substring(1);
        if (!targetId) return;
        var target = document.getElementById(targetId);
        if (!target) return;
        e.preventDefault();
        setActive(targetId);
        scrollToTarget(target);
        if (history.pushState) {
          history.pushState(null, null, "#" + targetId);
        } else {
          location.hash = "#" + targetId;
        }
      });
    });
  }

  function initScrollSpy() {
    if (allEntries.length === 0) return;

    function updateActive() {
      var scrollPos = window.scrollY + getHeaderOffset();
      var activeEntry = allEntries[0];

      for (var i = 0; i < allEntries.length; i++) {
        if (scrollPos >= allEntries[i].element.offsetTop) {
          activeEntry = allEntries[i];
        }
      }

      if (activeEntry) {
        setActive(activeEntry.id);
      }
    }

    var scrollTimeout;
    window.addEventListener("scroll", function () {
      if (scrollTimeout) clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(updateActive, 80);
    });

    updateActive();
  }
})();
