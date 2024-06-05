frappe.ui.form.on('Purchase Order',{
    refresh:function(frm){
        
        if(frm.doc.docstatus==1){
            frm.add_custom_button(__('Sales Order'), () => frm.trigger('create_so'), __('Create'));
        }
        
    },
    create_so:function(frm){
        var doc = frappe.model.get_new_doc('Sales Order');
        frappe.call({
            args:{
                doc:frm.doc.name
            },
            method: 'old_levene.utils.convert_to_so',
            callback: function(r) {
                let si_doc=r.message
				frappe.model.sync(r.message)
				// console.log(r.message)

				frappe.set_route("Form","Sales Order",si_doc.name);
            }
        });
		// doc.items = frm.doc.items
        // doc.inter_company_order_reference = frm.doc.name
		// frappe.set_route('Form', 'Sales Order', doc.name);
    }

})