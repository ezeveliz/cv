module.exports = function (eleventyConfig) {
    // Passthrough copy for assets
    eleventyConfig.addPassthroughCopy("assets");

    // Alias 'layout: cv' to '_layouts/cv.html'
    // Eleventy matches layouts in _includes by default, but we can config that.
    // Actually, for Jekyll compatibility, it searches _includes. 
    // We will tell it that _layouts is the includes dir, or better yet, just point the input.

    return {
        dir: {
            input: ".",
            includes: "_layouts", // Use _layouts as the includes directory for layouts
            output: "_site"
        },
        // Switch to liquid to match Jekyll
        templateFormats: ["md", "html", "liquid"],
        markdownTemplateEngine: "liquid",
        htmlTemplateEngine: "liquid"
    };
};
