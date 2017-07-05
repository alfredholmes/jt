function changephoto(src, title, description){
	photo = document.getElementById('mainphoto');

	photo.src = src
	photo.alt = title

	phototitle = document.getElementById('photo_title')
	photodescription = document.getElementById('photo_description')


	if(title)
	{
		phototitle.innerHTML = title
	}else{
		phototitle.innerHTML = ' '
	}
	if(description)
	{
		photodescription.innerHTML = description
	}else{
		photodescription.innerHTML = ' '
	}
}
