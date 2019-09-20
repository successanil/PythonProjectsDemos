var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/node-blog");

var Post = '';

var createModels = () => {
  var postSchema = new mongoose.Schema({ body: String });
  Post = mongoose.model("Post", postSchema);
};

module.exports = {
    createModels,
    Post
}
