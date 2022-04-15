        var count = 1

        function add_todo(title,date_time){


            document.getElementById("todo_list").innerHTML += `
                                                            <div id='todo_${count}' class="todo-item my-2 p-4 bg-light border border-light card">
                                                                <div class="">
                                                                        <h4 style="float:left" class="m-0 p-0">${title}</h4>
                                                                        <div style="float: right;">
                                                                            <i style="cursor: pointer;" onclick='delete_todo("${count}")' class="fas text-danger fa-trash"></i>
                                                                        </div>
                                                                </div>
                                                                <small class="text-muted">${date_time}</small>
                                                        </div>
            `

            count += 1

        }

        function delete_todo(id){
            $("#todo_" + id).slideUp()            


            //ajjax

            setTimeout(function(){
                $("#todo_" + id).remove()
            },2000)
            
        }
        
        $("#todo-form").submit(function(){

            var title = document.getElementById("title-input").value
            var date_time = document.getElementById("date-input").value + " " + document.getElementById("time-input").value
            
            add_todo(title, date_time)

            //ajax


            document.getElementById("todo-form").reset()
            return false
        })