function ViewModel() {
    var self = this;

    self.year = ko.observable('');
    self.month = ko.observable('');
    self.day = ko.observable('');
    self.blog_html = ko.observable('<h1 class="text-muted"><i class="fa fa-cog fa-spin"></i> loading...</h1>');
    self.title = ko.observable('');
    self.permalink = ko.observable('');
    self.map = ko.observableArray();

    self.updateBlogPost = function(data) {
        self.month(data.month);
        self.blog_html(data.html);
        self.title(data.title);
        self.year(data.year);
        self.day(data.day);
        self.permalink(data.permalink);
        $('pre code').each(function(i, e) {hljs.highlightBlock(e)});
    };

    self.fetchBlog = function(data) {
        self.updateBlogPost(data);
    };
};
    

vm = new ViewModel();

$(document).ready(function() {
    // get the latest blog post
    $.getJSON('/api/blog/latest', function (response){
        vm.updateBlogPost(response);
    });
    // get a map of all blog posts
    $.getJSON('/api/blog/map', function (response){
        vm.map(response);
    });
});

ko.applyBindings(vm);

// smooth scrolling from one #id to another #id on the page
$(function() {
    $('a[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
            || location.hostname == this.hostname) {
        
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });
});
