import { Storage } from "aws-amplify";

export async function s3Upload(file, personID, personName) {
  personName = personName.replace(" ", "_");
  const filename = `${personID}-${personName}-${file.name}`;

  const stored = await Storage.vault.put(filename, file, {
    contentType: file.type
  });

  return stored.key;
}
