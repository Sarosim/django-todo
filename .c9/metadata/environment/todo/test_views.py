{"filter":false,"title":"test_views.py","tooltip":"/todo/test_views.py","undoManager":{"mark":15,"position":15,"stack":[[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["T"],"id":2},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["o"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["D"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["o"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["I"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["t"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["e"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["m"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["F"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["o"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["r"]}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["m"],"id":3}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["V"],"id":4},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["i"]},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["e"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["w"]}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["s"],"id":5}],[{"start":{"row":6,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["    def test_can_create_an_item_with_just_a_name(self):","        form = ItemForm({'name': 'Create Tests'})","        self.assertTrue(form.is_valid())","    ","    def test_correct_message_for_missing_name(self):","        form = ItemForm({'form': ''})","        self.assertFalse(form.is_valid())","        self.assertEqual(form.errors['name'], [u'This field is required.'])",""],"id":6},{"start":{"row":6,"column":0},"end":{"row":26,"column":47},"action":"insert","lines":["    def test_get_home_page(self):","        page = self.client.get(\"/\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"todo_list.html\")","    ","    def test_get_add_item_page(self):","        page = self.client.get(\"/add\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"item_form.html\")","    ","    def test_get_edit_item_page(self):","        item = Item(name=\"Create a Test\")","        item.save()","","        page = self.client.get(\"/edit/{0}\".format(item.id))","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"item_form.html\")","    ","    def test_get_edit_page_for_item_that_does_not_exist(self):","        page = self.client.get(\"/edit/1\")","        self.assertEqual(page.status_code, 404)"]}],[{"start":{"row":1,"column":27},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":24},"action":"insert","lines":["from .models import Item"],"id":8}],[{"start":{"row":27,"column":47},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]},{"start":{"row":28,"column":8},"end":{"row":29,"column":0},"action":"insert","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":29,"column":4},"end":{"row":52,"column":41},"action":"insert","lines":["    def test_post_create_an_item(self):","        response = self.client.post(\"/add\", {\"name\": \"Create a Test\"})","        item = get_object_or_404(Item, pk=1)","        self.assertEqual(item.done, False)","    ","    def test_post_edit_an_item(self):","        item = Item(name=\"Create a Test\")","        item.save()","        id = item.id","","        response = self.client.post(\"/edit/{0}\".format(id), {\"name\": \"A different name\"})","        item = get_object_or_404(Item, pk=id)","","        self.assertEqual(\"A different name\", item.name)","    ","    def test_toggle_status(self):","        item = Item(name=\"Create a Test\")","        item.save()","        id = item.id","","        response = self.client.post(\"/toggle/{0}\".format(id))","","        item = get_object_or_404(Item, pk=id)","        self.assertEqual(item.done, True)"],"id":10}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":8},"action":"remove","lines":["    "],"id":11}],[{"start":{"row":2,"column":24},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":6,"column":24},"action":"insert","lines":["from django.test import TestCase","from django.shortcuts import get_object_or_404","from .models import Item"],"id":13}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["from django.test import TestCase",""],"id":14}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["from .forms import ItemForm",""],"id":15}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["from .models import Item",""],"id":16}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":17}]]},"ace":{"folds":[],"scrolltop":445,"scrollleft":0,"selection":{"start":{"row":53,"column":45},"end":{"row":53,"column":45},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":30,"state":"start","mode":"ace/mode/python"}},"timestamp":1572552777052,"hash":"8cf800826ec9bc08aa4c9d2f2782dd7f504752f4"}