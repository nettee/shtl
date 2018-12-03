use std::env;
use std::error::Error;
use std::fs::File;
use std::io::Read;
use std::io::Write;
use std::process::exit;

struct Args {
    in_file_name: String,
    out_file_name: String,
}

impl Args {
    fn parse() -> Result<Args, &'static str> {
        let args: Vec<String> = env::args().collect();
        if args.len() != 3 {
            return Err("cp: missing file operand");
        }

        Ok(Args {
            in_file_name: args[1].clone(),
            out_file_name: args[2].clone(),
        })
    }
}

fn run(args: Args) -> Result<(), Box<Error>> {
    let mut in_file = File::open(args.in_file_name)?;
    let mut out_file = File::create(args.out_file_name)?;

    let mut buffer = [0; 4096];

    loop {
        let n = in_file.read(&mut buffer)?;
        if n == 0 {
            break;
        }
        out_file.write(&buffer)?;
    }

    Ok(())
}

fn main() {
    let args = Args::parse().unwrap_or_else(|err| {
        eprintln!("{}", err);
        exit(1);
    });

    if let Err(err) = run(args) {
        eprintln!("{}", err);
        exit(1);
    }
}