const AboutPage = () => {
  return (
    <div className="bg-white p-8 border border-gray-800 flex-auto space-y-5">
      <a href="/" className="flex items-center">
  <svg className="w-4 h-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18">
    </path>
  </svg>
  Return Home Page
</a>

      <h1 className="text-3xl font-bold mb-4 text-center">
        What is Glaucoma? How it happens
      </h1>

      <div className="flex">
        <div className="size-11/12">
          <img
            src="/assets/gluacoma.jpg"
            alt="GlaucomaImage"
            className="mb-4"
          />
        </div>
        <div className="flex-col">
          <h1 className="text-3xl font-bold text-center text-start pl-7 pb-3 pt-7">
            What is Glaucoma (Glaucoma surgery)?
          </h1>
          <p className="text-xl mb-4 text-center text-start pl-7">
            Glaucoma is an eye disease that can damage your optic nerve which is
            situated at the back of the eye. That optic nerve supplies visual
            information to your brain from your eyes. It usually happens when
            fluid builds up in the front part of your eye. That extra fluid
            increases the pressure in your eye, damaging the optic nerve. And
            this damage to the optic nerve could result in blindness.
          </p>
        </div>
      </div>

      <h2 className="text-3xl font-bold mb-4 text-center">What are the Causes of this Disease:</h2>

  <div className="flex">
  <div className="flex-1">
    <div className="flex flex-col">
      <p className='text-3xl mb-4 text-center text-start '>It can occur for several reasons.</p>
      <ul>
        <li>Family history of Glaucoma</li>
        <li>Poor or reduced blood flow to your optic nerve</li>
        <li>High Blood Pressure</li>
        <li>Blunt or chemical injury to eyes</li>
        <li>Severe eye infection</li>
        <li>Blocked blood vessels inside your eyes</li>
        <li>Inflammatory conditions</li>
      </ul>
    </div>
  </div>
  <div className="ml-auto">
    <img src="/assets/infection.jpg" alt="Severe Eye Infection" />
  </div>
</div>


    </div>
  );
};

export default AboutPage;
