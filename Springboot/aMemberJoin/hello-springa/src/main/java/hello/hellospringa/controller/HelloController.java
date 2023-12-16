package hello.hellospringa.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {

    @GetMapping("you")
    public String hello(Model model){
        model.addAttribute("data", "you!");
        return "you";

    }

}
