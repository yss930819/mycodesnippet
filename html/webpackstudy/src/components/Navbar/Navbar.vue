<template>
  <div class="navbar navbar-inverse navbar-extra">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
        <a class="navbar-brand" href="/">LeetCode</a>
      </div>
      <div class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <li id="subscribe">
            <a href="/subscribe/">
              <font color="orange">Subscribe</font>
            </a>
          </li>

          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
                  Problems
                  <span class="caret"></span>
                </a>
            <ul class="dropdown-menu" role="menu">


              <li><a href="/problemset/algorithms/">Algorithms</a></li>



              <li><a href="/problemset/database/">Database</a></li>



              <li><a href="/problemset/shell/">Shell</a></li>



              <li><a href="/problemset/draft/">Draft</a></li>




              <li role="separator" class="divider"></li>
              <li><a href="/library/application/">Add Question</a></li>
            </ul>
          </li>

          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
                    Mock
                    <span class="caret"></span>
                  </a>
            <ul class="dropdown-menu">
              <li>
                <a href="/mockinterview/">Mock Interview</a>
              </li>
              <li>
                <a href="/mockinterview/session/list/">Past Sessions</a>
              </li>
            </ul>
          </li>



          <li><a href="/contest/">Contest</a></li>



          <li id="coursesNav"><a href="/courses/">Courses</a></li>

          <li id="articlesNav"><a href="/articles/">Articles</a></li>
          <!-- TODO: not hard code -->

          <li id=""><a href="https://discuss.leetcode.com" target="_blank">Discuss</a></li>


          <li id="bookNav" class="hidden-sm">
            <a onclick="ga('send', 'event', 'book', 'click', 'nav-bar');" href="/book/">
              <font color="#ed9c28">Book</font>
            </a>
          </li>




        </ul>

        <div class="navbar-form navbar-right">
          <a class="btn btn-primary" href="/accounts/signup">Sign up</a>
          <a class="btn btn-default" href="/accounts/login/">Sign in</a>
        </div>

        <!--
            <form class="navbar-form pull-right">
              <input class="col-md-2" type="text" placeholder="Email">
              <input class="col-md-2" type="password" placeholder="Password">
              <button type="submit" class="btn">Sign in</button>
            </form>
            -->
      </div>
      <!--/.navbar-collapse -->
    </div>
  </div>
</template>

<script>
  export default {
    name: 'my-navbar',
    data: function () {
      return {
        msg: 100,
      }
    }
  }

</script>

<style scoped>
.navbar{
  border-radius: 0px;
}
</style>
