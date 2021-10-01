$( document ).ready(function() {
    let key = $("#key").val()
    $(".keyword").html(key)


 
});


function getListByCate(page){
//    let idcate =$("#idcate").val()
//    url = '/polls/category/'+idcate
//    window.location.href=url
}

function getListHotproductsApi(e){
    $(".filter").each(function(){
        $(this).removeClass('btn--primarys');
    });
    $(e).addClass('btn--primarys');
    let pagecurent = 1;
    let key = $("#key").val()
    $.ajax({
        url: '/polls/hotproductsSearchApi?pagecurent='+pagecurent+'&key='+key,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            console.log("hot",res.first_products)
            showData(res.first_products)
            // paging(Math.ceil(res.totalItem/10),1)
        },
        error: function (res) {
            console.log(res)
        }
    });
}

function getListSoldProduct(e){
    $(".filter").each(function(){
        $(this).removeClass('btn--primarys');
    });
    $(e).addClass('btn--primarys');
    let pagecurent = 1;
    let key = $("#key").val()
    $.ajax({
        url: '/polls/soldproductsSearchApi?pagecurent='+pagecurent+'&key='+key,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            console.log("sold",res.first_products)
            showData(res.first_products)
            // paging(Math.ceil(res.totalItem/10),1)
        },
        error: function (res) {
            console.log(res)
        }
    });
}

function getListProductOrderByPriceDesc(){
    let pagecurent = 1;
    let key = $("#key").val()
    let orderBy = 1
    $.ajax({
        url: '/polls/productsOrderBySearchApi?pagecurent='+pagecurent+'&key='+key+'&orderBy='+orderBy,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            console.log("dessc",res.first_products)
            showData(res.first_products)
            // paging(Math.ceil(res.totalItem/10),1)
        },
        error: function (res) {
            console.log(res)
        }
    });
}


function getListProductOrderByPriceEsc(){
    let pagecurent = 1;
    let key = $("#key").val()
    let orderBy = 0
    $.ajax({
        url: '/polls/productsOrderBySearchApi?pagecurent='+pagecurent+'&key='+key+'&orderBy='+orderBy,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            console.log("essc",res.first_products)
            showData(res.first_products)
            // paging(Math.ceil(res.totalItem/10),1)
        },
        error: function (res) {
            console.log(res)
        }
    });
}


function showData(res){
    let data = ``
    if(res.length>0){
        $.each(res,function(k,v){
            let saleprice = v[2]*v[3]
            let discount = (v[3]!=1) ?  v[3]*100 : 0
            data +=`
              <div class="gird__col-2-4">
                      <a href="/polls/products/${v[0]}" class="home-product-item">
                          <div class="home-product-item__img" style="background-image: url(/static/img/${v[7]})">
                          </div>
                          <div class="home-product-item__info">
                              <h4 class="home-product-item__name">${v[1]}</h4>
                              <div class="home-product-item__price">
                                  <span class="home-product-item__price-old">
                                       ${v[2]}
                                  </span>
                                  <span class="home-product-item__price-current">
                                     ${saleprice}
                                  </span>
                              </div>
                              <div class="home-product-item__action">
                                  <div class="home-product-item__action-like home-product-item__action-liked">
                                      <i class="far fa-heart icon-product-nolike"></i>
                                      <i class="fas fa-heart icon-product-like"></i>
                                  </div>
                                  <div class="home-product-item__action-rate">
                                      <i class="fas fa-star home-product-item__star-gold"></i>
                                      <i class="fas fa-star home-product-item__star-gold"></i>
                                      <i class="fas fa-star home-product-item__star-gold"></i>
                                      <i class="fas fa-star"></i>
                                      <i class="fas fa-star"></i>
                                  </div>
                                  <span class="home-product-item__sold">${v[6]} đã bán</span>
                              </div>
                              <!-- <div class="home-product-item__origin">
                                  <div class="home-product-item__orgin-brand">Gucci</div>
                                  <div class="home-product-item__orgin-country">USA</div>
                              </div>
                              <div class="home-product-item__favourite">
                                  <i class="fas fa-check"></i>
                                  <span>Yêu thích</span>
                              </div> -->
                              <div class="home-product-item__sale">
                                  <span class="home-product-item__sale-percent" style="font-size: 12px;"> ${discount}%</span>
                                  <span class="home-product-item__sale-lable">GIẢM</span>
                              </div>
                          </div>
                          
                      </a>
                  </div>
              `
      
              
             
          })
    }else data+=`
        <div style="padding:10px">
           <p style="color:red">Không có sản phẩm nào !</p>
        </div>
    `
    $(".grid_row_data").html(data)
}

