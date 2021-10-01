$( document ).ready(function() {

    let url='/polls/getAllBillApi'
  
    $.ajax({
        url: url,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            console.log(res)
            showAllOrder(res.listOrderByIdUser)
            showAllOrderWait(res.listOrderWaitPayment)
            showAllOrderPaid(res.listOrderPaid)
            showAllOrderCancel(res.listOrderCancel)

        },
        error: function (res) {
            console.log(res)
        }
    });

 
});



function showAllOrder(orders){

    
    let data = ``
    $.each(orders,function(k,v){
       let status = ``
       if(v[6]==0) status+=`Đơn hàng chờ thanh toán`
       else if (v[6]==1) status+=`Đơn hàng đã thanh toán`
       else status+=`Đơn hàng đã hủy`
       data+=`
       <div class="row" style=" border-bottom: 1px dotted rgba(0,0,0,.09);
            margin-top: 20px;
            padding-bottom: 22px;">
            <div class="d-flex">
                <div style="margin-right: 22px;">
                    <img class="img-responsive" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/5fafbb923393b712b96488590b8f781f.png" style="max-width: 100px; max-height: 100px;">
                </div>
                <div style="width: 600px;">
                    <h4>Mã hóa đơn : ${v[0]}</h4>
                    <p style="margin: 0px;"></p>
                    <p style="margin: 0px;">Ngày tạo : ${v[2]}</p>
                </div>
            </div>
            <div class="row w-100" style="margin-top: 20px;">
                <div class="col col-sm-4"><span>${status}</span></div>
                <div class="col col-sm-4"></div>
                <div class="col col-sm-4">  `;
            if(v[6]==1){
                data+=`
                <div class="checkout d-flex justify-content-end">
                <div>
                    <button class="btn btn-primary" style="margin-right: 15px;
                    width: 139px;
                    border: none;
 
                    background-color: #cd3011;"><a href="/polls/" style="color: white; text-decoration: none;">Mua lần nữa</a></button>
                </div>
                <div>
                    <button class="btn btn-primary" style="margin-right: 15px;
                    width: 139px;    border: solid 1px black;
                    background-color: white;" idcart="${v[4]}" onclick="showBill(this)"><span style="color: black;">Xem chi tiết</span></button>
                </div> 
            
                <div>
                    <button class="btn btn-primary" style="margin-right: 15px;
                    width: 139px;    border: solid 1px black;
                    background-color: #cd3011;border: none;"><span style="color: white;" idcart="${v[4]}" onclick="danhgia(this)">Đánh giá</span></button>
                </div>
            </div>
                `
            }else if(v[6]==0){
                data+=`
        

                <div class="checkout d-flex justify-content-end">
               <div>
               <button class="btn btn-primary" style="margin-right: 15px;
                   width: 139px;
                   border: solid 1px black;
                   background-color: #cd3011;"><a href="/polls/" style="color: white; text-decoration: none;">Mua lần nữa</a></button>
               </div>
               <div>
               <button class="btn btn-primary" style="margin-right: 15px;
                   width: 139px;    border: solid 1px black;

                   background-color: white;" idcart="${v[4]}" onclick="showBill(this)"><span style="color: black;">Xem chi tiết</span></button>
               </div>
               <div>
               <button class="btn btn-primary" style="margin-right: 15px;
                   width: 139px;    border: solid 1px black;

                   background-color: white;"><span style="color: black;"  status="2" id=${v[0]} onclick="huyBill(this)">Hủy đơn hàng</span></button>
               </div>
                </div>
                `
            }else{
                data+=`
                <div class="checkout d-flex justify-content-end">
                <div>
                    <button class="btn btn-primary" style="margin-right: 15px;
                    width: 139px;
                    border: none;

                    background-color: #cd3011;"><a href="/polls/" style="color: white; text-decoration: none;">Mua lần nữa</a></button>
                </div>
                <div>
                    <button class="btn btn-primary" style="margin-right: 15px;
                    width: 139px;    border: solid 1px black;
                    background-color: white;" idcart="${v[4]}" onclick="showBill(this)"><span style="color: black;">Xem chi tiết</span></button>
                </div> 
            
            </div>
                
                `
            }
               

            data+=` </div>
            </div>
            </div>`

    })

    $(".listOrderAll").html(data)
}

function showAllOrderWait(orders){

    let data = ``
    $.each(orders,function(k,v){
       let status = ``
       if(v[6]==0) status+=`Đơn hàng chờ thanh toán`
       else if (v[6]==1) status+=`Đơn hàng đã thanh toán`
       else status+=`Đơn hàng đã hủy`
       data+=`
       <div class="row" style=" border-bottom: 1px dotted rgba(0,0,0,.09);
            margin-top: 20px;
            padding-bottom: 22px;">
            <div class="d-flex">
                <div style="margin-right: 22px;">
                    <img class="img-responsive" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/5fafbb923393b712b96488590b8f781f.png" style="max-width: 100px; max-height: 100px;">
                </div>
                <div style="width: 600px;">
                    <h4>Mã hóa đơn : ${v[0]}</h4>
                    <p style="margin: 0px;"></p>
                    <p style="margin: 0px;">Ngày tạo : ${v[2]}</p>
                </div>
            </div>
            <div class="row w-100" style="margin-top: 20px;">
                <div class="col col-sm-4"><span>${status}</span></div>
                <div class="col col-sm-4"></div>
                <div class="col col-sm-4">
                    <div class="checkout d-flex justify-content-end">
                        <div>
                        <button class="btn btn-primary" style="margin-right: 15px;
                            width: 139px;
                            border: solid 1px black;
                            background-color: #cd3011;"><a href="/polls/" style="color: white; text-decoration: none;">Mua lần nữa</a></button>
                        </div>
                        <div>
                        <button class="btn btn-primary" style="margin-right: 15px;
                            width: 139px;    border: solid 1px black;

                            background-color: white;" idcart="${v[4]}" onclick="showBill(this)"><span style="color: black;">Xem chi tiết</span></button>
                        </div>
                        <div>
                        <button class="btn btn-primary" style="margin-right: 15px;
                            width: 139px;    border: solid 1px black;

                            background-color: white;"><span style="color: black;" id=${v[0]} status="2" onclick="huyBill(this)">Hủy đơn hàng</span></button>
                        </div>
                    </div>
                </div>
            </div>
            </div>
       `

    })

    $(".listOrderAllWait").html(data)
}



function huyBill(e){
    let idorder = $(e).attr("id")
    let url='/polls/updateOrderApi?idorder='+idorder
    if(confirm("Bạn muốn hủy đơn hàng này ?")){
        $.ajax({
            url: url,
            method:'get',
            dataType: 'json',
            contentType: "application/json",
            success: function (res) {
                alert("Hủy đơn hàng thành công !")
                location.reload()
            },
            error: function (res) {
                console.log(res)
            }
        });
    }
    
}


function danhgia(e){
    let idcart = $(e).attr("idcart")
    
    let url='/polls/getDetailOrderApi?idcart='+idcart
  
    $.ajax({
        url: url,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            console.log(res)
            let data = ``
            $.each(res,function(k,v){
               
                data+=`
                <div class="row" style=" border-bottom: 1px dotted rgba(0,0,0,.09);
                margin-top: 20px;
                padding-bottom: 22px;     margin-left: 6px;">
                <div class="d-flex col col-sm-12">
                   <div style="margin-right: 22px;">
                      <img class="img-responsive" src="/static/img/${v[4]}" style="max-width: 100px; max-height: 100px;">
                   </div>
                   <div style="width: 600px;">
                      <h6  class="mb-2" style="font-size: 15px;">Tên sản phẩm : ${v[6]}</h6>
                      <p style="margin: 0px;"  class="mb-2"> số lượng mua : x${v[3]}</p>
                      <p style="margin: 0px;" class="mb-5">Tổng : ${v[7]} </p>
                      <div class=" col col-sm-12 p-0 mb-3">
                         <ul class="ratings d-flex p-0">
                            <i class="fa fa-star star_1_${v[0]} star_${v[0]}" aria-hidden="true" style="font-size: 15px; color: rgb(0 0 0 / 28%);" vote="1" idorder=${v[0]} idproduct=${v[1]} onclick="vote(this)"></i>
                            <i class="fa fa-star star_2_${v[0]} star_${v[0]}" aria-hidden="true" style="font-size: 15px; color: rgb(0 0 0 / 28%);" vote="2" idorder=${v[0]} idproduct=${v[1]} onclick="vote(this)"></i>
                            <i class="fa fa-star star_3_${v[0]} star_${v[0]}" aria-hidden="true" style="font-size: 15px; color: rgb(0 0 0 / 28%);" vote="3" idorder=${v[0]} idproduct=${v[1]} onclick="vote(this)"></i>
                            <i class="fa fa-star star_4_${v[0]} star_${v[0]}" aria-hidden="true" style="font-size: 15px; color: rgb(0 0 0 / 28%);" vote="4" idorder=${v[0]} idproduct=${v[1]} onclick="vote(this)"></i>
                            <i class="fa fa-star star_5_${v[0]} star_${v[0]}" aria-hidden="true" style="font-size: 15px; color: rgb(0 0 0 / 28%);" vote="5" idorder=${v[0]} idproduct=${v[1]} onclick="vote(this)"></i>
                         </ul>
                         <input type="hidden" class="value_vote_${v[1]}" />
                      </div>
                      <div class="binhluan col col-sm-12 p-0">
                         <textarea id="comment_${v[1]}" name="w3review" rows="4" cols="50" class="form-control" placeholder="Nhập bình luận của bạn"></textarea>
                      </div>
 
                      <div class="col col-sm-12 p-0">
                         <div class="d-flex justify-content-end">
                            <button class="btn btn-primary" style="margin-top: 15px;
                               width: 139px;
                               border: none;  
                               background-color: #cd3011;"><a href="#" style="color: white; text-decoration: none;" idproduct="${v[1]}" onclick="comment(this)">Đánh giá</a></button>
                         </div>
                      </div>
                   </div>
                </div>
             </div>
            `
            })
            $(".votes").html(data)
            $("#danhgias").modal("show")
  
        },
        error: function (res) {
            console.log(res)
        }
    });


    
 }

function comment(e){
    
    let idproduct=$(e).attr("idproduct")
    let comment = $(`#comment_`+idproduct).val()
    let vote = $(`.value_vote_`+idproduct).val()
    let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();	
    var data = new FormData();  
    data.append("idproduct",idproduct)  
    data.append("comment",comment)  
    data.append("vote",vote)
    data.append("csrfmiddlewaretoken", csrf_token);
    console.log(idproduct+"-"+comment+"-"+vote)
    if(vote&&comment){
        $.ajax({
            url: '/polls/voteApi',
            method:'POST',
            data:data,
            cache: false,                                               //Upload files without caching
            processData:false,                                          //Do not serialize data
            contentType:false, 
            success: function (res) {
                console.log(res)
                $(`#comment_`+idproduct).val("")
                alert("Cám ơn bạn đã phản hồi về sản phẩm này !")
            },
            error: function (res) {
                console.log(res)
               //  window.location.href="/polls/"
            }
        });
    }else alert("Vui lòng đánh giá và bình luận sản phẩm ?")
}

function vote(e){
    let idorder = $(e).attr("idorder")
    let idproduct = $(e).attr("idproduct")
    let classNameValueVote = '.value_vote_'+idproduct
    let className = '.star_'+idorder
    let vote = $(e).attr("vote")
    
    $(".selectedStar").each(function(){
        $(this).removeClass('selectedStar');
    });
    for(let i = 1 ; i<=vote ;i++){
       let classStar = `.star_`+i+`_`+idorder
       $(classStar).addClass("selectedStar")
      
    }
    $(classNameValueVote).val(vote)
}


function showAllOrderPaid(orders){

    let data = ``
    $.each(orders,function(k,v){
       let status = ``
       if(v[6]==0) status+=`Đơn hàng chờ thanh toán`
       else if (v[6]==1) status+=`Đơn hàng đã thanh toán`
       else status+=`Đơn hàng đã hủy`
       data+=`
       <div class="row" style=" border-bottom: 1px dotted rgba(0,0,0,.09);
            margin-top: 20px;
            padding-bottom: 22px;">
            <div class="d-flex">
                <div style="margin-right: 22px;">
                    <img class="img-responsive" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/5fafbb923393b712b96488590b8f781f.png" style="max-width: 100px; max-height: 100px;">
                </div>
                <div style="width: 600px;">
                    <h4>Mã hóa đơn : ${v[0]}</h4>
                    <p style="margin: 0px;"></p>
                    <p style="margin: 0px;">Ngày tạo : ${v[2]}</p>
                </div>
            </div>
            <div class="row w-100" style="margin-top: 20px;">
                <div class="col col-sm-4"><span>${status}</span></div>
                <div class="col col-sm-4"></div>
                <div class="col col-sm-4">  

                <div class="checkout d-flex justify-content-end">
                    <div>
                        <button class="btn btn-primary" style="margin-right: 15px;
                        width: 139px;
                        border: none;
                        
                        background-color: #cd3011;"><a href="/polls/" style="color: white; text-decoration: none;">Mua lần nữa</a></button>
                    </div>
                    <div>
                        <button class="btn btn-primary" style="margin-right: 15px;
                        width: 139px;    border: solid 1px black;
                        background-color: white;" idcart="${v[4]}" onclick="showBill(this)"><span style="color: black;">Xem chi tiết</span></button>
                    </div> 
                
                    <div>
                        <button class="btn btn-primary" style="margin-right: 15px;
                        width: 139px;    border: solid 1px black;
                        background-color: #cd3011;border: none;"><span style="color: white;" idcart="${v[4]}" onclick="danhgia(this)">Đánh giá</span></button>
                    </div>
                </div>

                </div>
            </div>
            </div>
       `

    })

    $(".listOrderAllPaid").html(data)
}

function showBill(e){
    let idcart = $(e).attr("idcart")
    
    let url='/polls/getDetailOrderApi?idcart='+idcart
  
    $.ajax({
        url: url,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            console.log(res)
            let data = ``
            let totalMoney = 0
            $.each(res,function(k,v){
                totalMoney+=v[7]
                data+=`
                <div class="row" style=" border-bottom: 1px dotted rgba(0,0,0,.09);
                    margin-top: 20px;
                    padding-bottom: 22px;     margin-left: 6px;">
                    <div class="d-flex">
                    <div style="margin-right: 22px;">
                        <img class="img-responsive" src="/static/img/${v[4]}" style="max-width: 100px; max-height: 100px;">
                    </div>
                    <div style="width: 600px;">
                        <h6 style="font-size:15px">Tên sản phẩm : tivi 2</h6>
                        <p style="margin: 0px;">số lượng mua : x${v[3]}</p>
                        <p style="margin: 0px;">Số tiền : ${v[7]} </p>
                    </div>
                    </div>
                </div>
                 
                `
            })
            data+=`
            <div class="row" style="margin-top: 20px;">
                <div class="col col-sm-4"><span></span></div>
                <div class="col col-sm-4"></div>
                <div class="col col-sm-4">
                <div class="checkout d-flex justify-content-end">
                    <div>
                        <span style="color: black;" class="totalMoney">Tổng tiền thanh toán : ${totalMoney}</span>
                    </div>
                </div>
                </div>
            </div>
            `
            $(".listSP").html(data)
            $("#showDetailBill").modal("show")

        },
        error: function (res) {
            console.log(res)
        }
    });

    
}

function showAllOrderCancel(orders){

    let data = ``
    $.each(orders,function(k,v){
       let status = ``
       if(v[6]==0) status+=`Đơn hàng chờ thanh toán`
       else if (v[6]==1) status+=`Đơn hàng đã thanh toán`
       else status+=`Đơn hàng đã hủy`
       data+=`
       <div class="row" style=" border-bottom: 1px dotted rgba(0,0,0,.09);
            margin-top: 20px;
            padding-bottom: 22px;">
            <div class="d-flex">
                <div style="margin-right: 22px;">
                    <img class="img-responsive" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/5fafbb923393b712b96488590b8f781f.png" style="max-width: 100px; max-height: 100px;">
                </div>
                <div style="width: 600px;">
                    <h4>Mã hóa đơn : ${v[0]}</h4>
                    <p style="margin: 0px;"></p>
                    <p style="margin: 0px;">Ngày tạo : ${v[2]}</p>
                </div>
            </div>
            <div class="row w-100" style="margin-top: 20px;">
                <div class="col col-sm-4"><span>${status}</span></div>
                <div class="col col-sm-4"></div>
                <div class="col col-sm-4">
                    <div class="checkout d-flex justify-content-end">
                        <div>
                            <button class="btn btn-primary" style="margin-right: 15px;
                            width: 139px;
                            border: none;
                            background-color: #cd3011;"><a href="/polls/" style="color: white; text-decoration: none;">Mua lần nữa</a></button>
                        </div>
                        <div>
                            <button class="btn btn-primary" style="margin-right: 15px;
                            width: 139px;    border: solid 1px black;
                            background-color: white;" idcart="${v[4]}" onclick="showBill(this)"><span style="color: black;">Xem chi tiết</span></button>
                        </div> 
                    
                    </div>
                </div>
            </div>
            </div>
       `

    })

    $(".listOrderAllCancel").html(data)
}
