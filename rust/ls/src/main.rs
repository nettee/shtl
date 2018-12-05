extern crate chrono;
extern crate nix;
extern crate users;

use std::env;
use std::error::Error;
use std::fs;
use std::path::Path;
use std::process::exit;

use stat::FileStat;

mod stat;

struct Args {
    files: Vec<String>,
}

impl Args {
    fn parse() -> Result<Args, &'static str> {
        let mut args = env::args();
        args.next();
        let files: Vec<String> = args.collect();
        Ok(Args { files })
    }
}


fn ls(item: &String) -> Result<(), Box<Error>> {
    let md = fs::metadata(item)?; // Corresponds to `stat` in Unix
    if md.is_dir() {
        println!("{}:", item);
        let dir = Path::new(&item);
        for entry in fs::read_dir(item)? {
            let entry = entry?;
            let file_name = entry.file_name();
            let name = file_name.to_string_lossy().into_owned();
            if name.chars().nth(0) == Some('.') {
                continue;
            }
            let full_path = dir.join(Path::new(&name));
            let stat = FileStat::new(&full_path)?;
            stat.print();
            println!("{}", name);
        }
    } else {
        println!("{}", item);
    }
    Ok(())
}

fn run(args: Args) -> Result<(), Box<Error>> {
    if args.files.is_empty() {
        ls(&String::from("."))?;
    } else if args.files.len() == 1 {
        ls(&args.files[0])?;
    } else {
        for item in args.files {
            ls(&item)?;
        }
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
