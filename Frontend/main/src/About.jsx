export default function About() {
    return (
        <div className='grid grid-cols-1 gap-20'>
            <div className='text-center font-black text-5xl'><h1>About</h1></div>
            <div className='grid grid-cols-2 justify-center gap-20 h-96'>
                <div className="border-4 w-full h-full rounded-xl"></div>
                <div className="grid grid-cols-1 py-10">
                    <div className="text-center font-bold text-2xl">About Porthree</div>
                    <div>
                        <p>Mauris nunc congue nisi vitae suscipit tellus mauris a. Vitae
                            auctor eu augue ut lectus. Purus viverra accumsan in nisl nisi scelerisque
                            eu. Iaculis urna id volutpat lacus.Mauris nunc congue nisi vitae suscipit
                            tellus mauris a. Vitae auctor eu augue ut lectus. Purus viverra accumsan in
                            nisl nisi scelerisque eu. Iaculis urna id volutpat lacus.</p>
                    </div>
                    <div><button className="border px-2 font-bold">Read More...</button></div>
                </div>
            </div>
        </div>
    )
}
