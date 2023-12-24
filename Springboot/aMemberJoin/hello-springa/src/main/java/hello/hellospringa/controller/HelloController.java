package hello.hellospringa.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HelloController {

    @GetMapping("you")
    public String hello(Model model){
        model.addAttribute("data", "you!");
        return "you";

    }

    @GetMapping("you-mvc")
    public String youMvc(@RequestParam("name") String name, Model model){
        model.addAttribute("name", name);
        return "you-template";
    }


}
