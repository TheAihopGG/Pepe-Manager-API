# API Reference

## Types of resources

### Package

- id
- name
- description
- version
- author_name
- created_at
- updated_at

### PackageData

- id
- package_id (FOREIGN KEY)
- data (bytes data)

## Urls

All urls are relative `<domain>://api_v1`

### Example

|Method|Url|Description|
|------|---|-----------|
|GET|`/example`|Example|

Request:
```json
{
    "key": "value"
}
```