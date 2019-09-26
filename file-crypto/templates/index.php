<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta charset="utf-8">
  <meta name="theme-color" content="#0a0b39">
  <title>File Cryptography</title>
 <!--  <link rel="icon" href="images/fevicon.png"> -->

  <link href="https://fonts.googleapis.com/css?family=Acme&display=swap" rel="stylesheet">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
  <!-- Bootstrap core CSS -->
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <!-- Material Design Bootstrap -->
  <link href="css/mdb.min.css" rel="stylesheet">
  <!-- Your custom styles (optional) -->
  <link href="css/style.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="css/responsive.css">

</head>

<body>

  <?php include 'header.php'; ?>

  <section>
      <!--Carousel Wrapper-->
      <div id="video-carousel-example2" class="carousel slide carousel-fade" data-ride="carousel">
        <!--Indicators-->
        <ol class="carousel-indicators">
          <li data-target="#video-carousel-example2" data-slide-to="0" class="active"></li>
          <li data-target="#video-carousel-example2" data-slide-to="1"></li>
          <li data-target="#video-carousel-example2" data-slide-to="2"></li>
        </ol>
        <!--/.Indicators-->
        <!--Slides-->
        <div class="carousel-inner" role="listbox">
          <!-- First slide -->
          <div class="carousel-item active">
            <!--Mask color-->
            <div class="view">
              <!--Video source-->
              <video class="video-fluid" autoplay loop muted>
                <source src="https://mdbootstrap.com/img/video/Lines.mp4" type="video/mp4" />
              </video>
              <div class="mask rgba-indigo-light"></div>
            </div>

            <!--Caption-->
            <div class="carousel-caption">
              <div class="animated fadeInDown">
                <h3 class="h3-responsive">Light mask</h3>
                <p>First text</p>
              </div>
            </div>
            <!--Caption-->
          </div>
          <!-- /.First slide -->

          <!-- Second slide -->
          <div class="carousel-item">
            <!--Mask color-->
            <div class="view">
              <!--Video source-->
              <video class="video-fluid" autoplay loop muted>
                <source src="https://mdbootstrap.com/img/video/animation-intro.mp4" type="video/mp4" />
              </video>
              <div class="mask rgba-purple-slight"></div>
            </div>

            <!--Caption-->
            <div class="carousel-caption">
              <div class="animated fadeInDown">
                <h3 class="h3-responsive">Super light mask</h3>
                <p>Secondary text</p>
              </div>
            </div>
            <!--Caption-->
          </div>
          <!-- /.Second slide -->

          <!-- Third slide -->
          <div class="carousel-item">
            <!--Mask color-->
            <div class="view">
              <!--Video source-->
              <video class="video-fluid" autoplay loop muted>
                <source src="https://mdbootstrap.com/img/video/Tropical.mp4" type="video/mp4" />
              </video>
              <div class="mask rgba-black-strong"></div>
            </div>

            <!--Caption-->
            <div class="carousel-caption">
              <div class="animated fadeInDown">
                <h3 class="h3-responsive">Strong mask</h3>
                <p>Third text</p>
              </div>
            </div>
            <!--Caption-->
          </div>
          <!-- /.Third slide -->
        </div>
        <!--/.Slides-->
        <!--Controls-->
        <a class="carousel-control-prev" href="#video-carousel-example2" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#video-carousel-example2" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
        <!--/.Controls-->
      </div>
      <!--Carousel Wrapper-->
  </section>

  <?php include 'footer.php'; ?>


  <!-- SCRIPTS -->
  <!-- JQuery -->
  <script type="text/javascript" src="js/jquery-3.4.1.min.js"></script>
  <!-- Bootstrap tooltips -->
  <script type="text/javascript" src="js/popper.min.js"></script>
  <!-- Bootstrap core JavaScript -->
  <script type="text/javascript" src="js/bootstrap.min.js"></script>
  <!-- MDB core JavaScript -->
  <script type="text/javascript" src="js/mdb.min.js"></script>

  <script type="text/javascript" src="js/custom.js"></script>

</body>

</html>