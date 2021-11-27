function sendMail(contactForm) {
    emailjs.send("Gmail_MP3", "Extrahand", {
        "from_name": contactForm.name.value,
        "message": contactForm.message.value,
        "from_email": contactForm.emailaddress.value});

    document.getElementById("mailform").reset();
    return false;  // To block from loading a new page
}