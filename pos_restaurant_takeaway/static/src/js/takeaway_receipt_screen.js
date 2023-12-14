/** @odoo-module **/
import { Component } from "@odoo/owl";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { OrderWidget } from "@point_of_sale/app/generic_components/order_widget/order_widget";
import { ReceiptHeader } from "@point_of_sale/app/screens/receipt_screen/receipt/receipt_header/receipt_header";

export class TakeAwayOrderReceipt extends ReceiptHeader {
    static template = "TakeAwayOrderReceipt";
    static components = {
        Orderline,
        OrderWidget,
        ReceiptHeader,
    };
}

