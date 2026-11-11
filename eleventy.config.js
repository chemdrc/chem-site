export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets", "src/css": "css", "src/js": "js" });
  return {
    dir: { input: "src", output: "_site", includes: "_includes", data: "_data" },
    htmlTemplateEngine: "njk",
    templateFormats: ["html", "njk", "md"],
  };
}
