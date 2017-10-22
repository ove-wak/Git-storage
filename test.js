/* function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} */
function reConstructBinaryTree(pre, vin)
{
    var head = TreeNode(pre[0]);
    var head_vin = vin.indexOf(pre[0]);
    if(head_vin == 0){
        head.left = null;
    }else{
        var pre_vin = vin.slice(0,head_vin);
        var pre_pre = pre.slice(1,1+head_vin);
        head.left = reConstructBinaryTree(pre_pre, pre_vin); 
    }
    if(head_vin == vin.length - 1){
        head.right = null;
    }else{
        var ri_vin = vin.slice(head_vin + 1);
        var ri_pre = pre.slice(head_vin + 1);
        head.right = reConstructBinaryTree(ri_pre, ri_vin); 
    }
    return head;
}