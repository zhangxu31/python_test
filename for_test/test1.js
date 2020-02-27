/**
 * 业务查询类封装，根据业务需求，如存在多个功能点有相似查询需求时，需对查询方法进行封装提取
 * @author 包7
 **/
define([ 'tool', 'jquery.extends' ], function(tool, je) {
    // 业务查询类20190315
    var frontQuery = {

        /**
         * @description 根据客户账号查询简称
         * @param in  string 客户账号
         * @param in Array  需要反向显示
         * */
        uniontxtChange:function(dom_id,chane_id,muticon,ss,dd){
            function isArrayFn(value){
                return Object.prototype.toString.call(value)==="[object Array]";
            }
            $(dom_id).textbox({onChange:function(newValue,oldValue){
                if(newValue===''){
                    return false;
                }else{
                    //调用接口
                    var isob=IsArrayFn(muticon);
                    if(isob){
                        //根据债券代码 返显 市场 币种  或者  根据账号 返显简称
                        var obj={};
                        obj.accountNo=newValue;
                        this.commondmethod(ss, ss, obj, dd,function(data){
                            for (var cc in isob){
                                $(cc).textbox('setValue',data[cc])
                            }
                        });

                    }else{
                        var obj={};
                        obj.bondNo=newValue;
                        this.commondmethod(ss, ss, obj, dd,function(data){
                            $(changed_id).textbox('setValue',data);
                        });

                    }

                }
            }})
        },
        /**
         * @description 重置下拉框的值
         * @param 
         * {compId}:组件ID
         * {dicId}:字典编号
         * {dicOptions}:字典值
         * {dicFlag}:包括/排除标志（0：包含，1：排除）
         * {needBlank}:是否显示“全部”
         */
         resetDic : function(compId,dicId,dicOptions,dicFlag,needBlank) {
        	if(dicId == undefined || dicOptions == undefined) {
        		GLOBAL.logOutput && console.log("字典为空或字典项为空，请重新检查！");
        		return false;
        	}
        	if(dic[dicId] == undefined) {
        		GLOBAL.logOutput && console.log("无当前字典项：" + dicId);
        		return false;
        	}
        	var curDic = dic[dicId];
        	//dic所有key值
        	var dicVals = Object.keys(curDic);
        	//所有options
        	var optionVals = dicOptions.split(",");
        	//重置字典data
        	var newData = [];
        	if(needBlank) {
        		newData.push({"name":"全部","value":""});
        	}else {
        		newData.push({"name":"空","value":""});
        	}
        	var tempVal = "";
        	var tempName = "";
        	//当为“包含”时，将下拉框的值改为“optionVals”
        	if(dicFlag == "0") {
        		for(var j=0;j<optionVals.length;j++) {
        			tempVal = optionVals[j];
        			tempName = tool.dicFormat(dicId,tempVal);
        			newData.push({"name":tempName,"value":tempVal});
        		}
        	}
        	//当为“排除”时，下拉框枚举值删除“optionVals”
        	if(dicFlag == "1") {
        		for(var k=0;k<dicVals.length;k++) {
        			//排除选项
        			if(optionVals.indexOf(dicVals[k]) == -1) {
        				tempVal = dicVals[k];
    	    			tempName = tool.dicFormat(dicId,tempVal);
    	    			newData.push({"name":tempName,"value":tempVal});
        			}
        		}
        	}
        	$(compId).combobox({
         		data:newData,
         		valueField:'value',
         		textField:'name'
         	});
        },
    };
        
    return frontQuery;
})