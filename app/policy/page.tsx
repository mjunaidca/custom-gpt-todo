import React from "react";

const page = () => {
  return (
    <div className="max-w-6xl w-full mx-auto p-4 py-8 flex flex-col items-center justify-center text-left">
      <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
        FastAPI Backend Privacy Policy
      </h1>
      <p className="leading-7 [&:not(:first-child)]:mt-6">
        This privacy policy applies to the use of the FastAPI Backend, detailing
        how we collect, use, and protect your personal data.
      </p>
      <h2 className="mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">
        Data Collection
      </h2>
      <p className="leading-7 [&:not(:first-child)]:mt-6">
        We collect minimal user data necessary for the effective operation of
        the service. This includes data inputted by users in the TODO tasks.
      </p>
      <h3 className="mt-8 scroll-m-20 text-2xl font-semibold tracking-tight">
        Use of Information
      </h3>
      <p className="leading-7 [&:not(:first-child)]:mt-6">
        Collected data is used solely for the purpose of providing and improving
        our service. We do not share or sell your personal information.
      </p>
      <h3 className="mt-8 scroll-m-20 text-2xl font-semibold tracking-tight">
        Data Security
      </h3>
      <p className="leading-7 [&:not(:first-child)]:mt-6">
        We are committed to protecting your data and have implemented robust
        security measures to prevent unauthorized access or disclosure.
      </p>
      <h3 className="mt-8 scroll-m-20 text-2xl font-semibold tracking-tight">
        Your Rights
      </h3>
      <ul className="my-6 ml-6 list-disc [&>li]:mt-2">
        <li>
          Access to your data: You can request to see the data we hold about
          you.
        </li>
        <li>
          Data correction: If you find that the data we have is inaccurate or
          incomplete, you can ask us to correct it.
        </li>
        <li>
          Data deletion: You can request us to delete your personal data from
          our systems.
        </li>
      </ul>
      <p className="leading-7 [&:not(:first-child)]:mt-6">
        If you have any questions or concerns about our privacy practices,
        please contact us.
      </p>
      <p className="leading-7 [&:not(:first-child)]:mt-6">
        This policy is subject to changes, which will be updated on this page.
        Your continued use of the service constitutes your agreement to this
        privacy policy and any updates.
      </p>
    </div>
  );
};

export default page;
