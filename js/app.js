// This is a simple *viewmodel* - JavaScript that defines the data and behavior of your UI

var viewModel = {
  month: ko.observable(''),
  content: ko.observable(''),
  title: ko.observable(''),
};

function updateViewModel(data) {
  viewModel.month(data.month);
  viewModel.content(data.content);
  viewModel.title(data.title);
}

$.getJSON("/api/blog/latest", function (result) {
    updateViewModel(result)
  });

$(".blog-link").click(function () {
  blog_ref = $(this).attr("rel")
  $.getJSON(blog_ref, function (result) {
    updateViewModel(result)
  });
});

ko.applyBindings(viewModel); // This makes Knockout get to work
