import fs from "fs";

fs.appendFile("my-file.txt", "Hello content!", (err) => {
  if (err) throw err;
  console.log("Saved!");
});

setTimeout(() => console.log("The end"), 30000);
